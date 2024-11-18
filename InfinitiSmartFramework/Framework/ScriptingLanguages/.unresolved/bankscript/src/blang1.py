import hashlib

class BankAccount:
    def __init__(self, owner, password, initial_balance):
        self.owner = owner
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()
        self.balance = initial_balance
        self.is_locked = False
        self.is_blocked = False
        self.is_frozen = False

    def deposit(self, amount):
        if not self.is_locked and not self.is_blocked:
            if amount > 0:
                self.balance += amount
                return "Deposit successful. New balance: " + str(self.balance)
            else:
                return "Invalid deposit amount."
        else:
            return "Account is locked or blocked. Cannot perform transaction."

    def withdraw(self, amount):
        if not self.is_locked and not self.is_blocked:
            if amount > 0 and amount <= self.balance:
                self.balance -= amount
                return "Withdrawal successful. New balance: " + str(self.balance)
            else:
                return "Invalid withdrawal amount or insufficient funds."
        else:
            return "Account is locked or blocked. Cannot perform transaction."

    def check_balance(self):
        return "Account balance for " + self.owner + ": " + str(self.balance)

    def authenticate(self, password):
        input_password_hash = hashlib.sha256(password.encode()).hexdigest()
        return input_password_hash == self.password_hash

    def lock_account(self):
        self.is_locked = True
        return "Account locked."

    def unlock_account(self):
        self.is_locked = False
        return "Account unlocked."

    def block_account(self):
        self.is_blocked = True
        return "Account blocked."

    def unblock_account(self):
        self.is_blocked = False
        return "Account unblocked."

    def freeze_account(self):
        self.is_frozen = True
        return "Account frozen."

    def unfreeze_account(self):
        self.is_frozen = False
        return "Account unfrozen."

    def change_password(self, old_password, new_password):
        if self.authenticate(old_password):
            self.password_hash = hashlib.sha256(new_password.encode()).hexdigest()
            return "Password changed successfully."
        else:
            return "Authentication failed. Cannot change password."

class BankLangInterpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, code):
        lines = code.split('\n')
        output = []
        for line in lines:
            tokens = line.split(' ')
            if tokens[0] == "CREATE":
                if len(tokens) == 4:
                    owner, password, initial_balance = tokens[1], tokens[2], int(tokens[3])
                    self.variables[owner] = BankAccount(owner, password, initial_balance)
                    output.append("Account created for " + owner)
                else:
                    output.append("Invalid CREATE statement")
            elif tokens[0] == "DEPOSIT":
                if len(tokens) == 3:
                    owner, amount = tokens[1], int(tokens[2])
                    if owner in self.variables:
                        output.append(self.variables[owner].deposit(amount))
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid DEPOSIT statement")
            elif tokens[0] == "WITHDRAW":
                if len(tokens) == 3:
                    owner, amount = tokens[1], int(tokens[2])
                    if owner in self.variables:
                        output.append(self.variables[owner].withdraw(amount))
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid WITHDRAW statement")
            elif tokens[0] == "BALANCE":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].check_balance())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid BALANCE statement")
            elif tokens[0] == "LOCK":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].lock_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid LOCK statement")
            elif tokens[0] == "UNLOCK":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].unlock_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid UNLOCK statement")
            elif tokens[0] == "BLOCK":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].block_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid BLOCK statement")
            elif tokens[0] == "UNBLOCK":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].unblock_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid UNBLOCK statement")
            elif tokens[0] == "FREEZE":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].freeze_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid FREEZE statement")
            elif tokens[0] == "UNFREEZE":
                if len(tokens) == 2:
                    owner = tokens[1]
                    if owner in self.variables:
                        output.append(self.variables[owner].unfreeze_account())
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid UNFREEZE statement")
            elif tokens[0] == "CHANGEPASSWORD":
                if len(tokens) == 4:
                    owner, old_password, new_password = tokens[1], tokens[2], tokens[3]
                    if owner in self.variables:
                        output.append(self.variables[owner].change_password(old_password, new_password))
                    else:
                        output.append("Account not found for " + owner)
                else:
                    output.append("Invalid CHANGEPASSWORD statement")
            # Add more operations here
            elif tokens[0] == "":
                output.append("...")
            else:
                output.append("Invalid statement")

        if output != "":
            return '\n'.join(output)
        elif output == []:
            return ""

# Example usage:
interpreter = BankLangInterpreter()
code = """
CREATE Alice secretpassword 1000
DEPOSIT Alice 500
WITHDRAW Alice 200
BALANCE Alice
LOCK Alice
UNLOCK Alice
BLOCK Alice
UNBLOCK Alice
FREEZE Alice
UNFREEZE Alice
CHANGEPASSWORD Alice secretpassword newsecretpassword
"""
if __name__ == "__main__":
    x = 0
    while True:
        code = input(f"{x:<4} (B1) >>> ")
        print(interpreter.interpret(code))
        x = x + 1 
