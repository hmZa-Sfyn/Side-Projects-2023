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
        self.loop_variables = {}

    def interpret(self, code):
        lines = code.split(';')
        output = []
        for line in lines:
            tokens = line.strip().split(' ')
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
            elif tokens[0] == "IF":
                if len(tokens) >= 4 and tokens[2] == "==" and len(tokens) % 2 == 0:  # Check if syntax is correct
                    variable = tokens[1]
                    expected_value = tokens[3]
                    operator = tokens[2]
                    if variable in self.variables:
                        current_value = self.variables[variable].balance if variable != "PASSWORD" else self.variables[variable].password_hash
                        if operator == "==":
                            if str(current_value) == expected_value:
                                for i in range(4, len(tokens), 2):
                                    if tokens[i] == "ELSE":
                                        output.extend(self.interpret(' '.join(tokens[i+1:])))
                                        break
                                    elif tokens[i] == "ELIF":
                                        if i + 2 < len(tokens):
                                            variable = tokens[i+1]
                                            expected_value = tokens[i+2]
                                            operator = tokens[i+3]
                                            current_value = self.variables[variable].balance if variable != "PASSWORD" else self.variables[variable].password_hash
                                            if operator == "==":
                                                if str(current_value) == expected_value:
                                                    output.extend(self.interpret(' '.join(tokens[i+4:])))
                                                    break
                                            else:
                                                output.append("Invalid operator in ELIF statement")
                                                break
                                        else:
                                            output.append("Incomplete ELIF statement")
                                            break
                                    elif tokens[i] == "ENDIF":
                                        break
                                    else:
                                        output.append("Invalid statement inside IF block")
                                        break
                        else:
                            output.append("Invalid operator in IF statement")
                    else:
                        output.append("Variable not found in IF statement")
                else:
                    output.append("Invalid IF statement")
            elif tokens[0] == "FOR":
                if len(tokens) == 5:
                    variable = tokens[1]
                    start_value = int(tokens[2])
                    end_value = int(tokens[3])
                    step = int(tokens[4])
                    if variable not in self.loop_variables:
                        self.loop_variables[variable] = start_value
                    else:
                        self.loop_variables[variable] += step
                    if self.loop_variables[variable] <= end_value:
                        for i in range(self.loop_variables[variable], end_value+1, step):
                            self.loop_variables[variable] = i
                            output.extend(self.interpret(' '.join(tokens[5:])))
                    else:
                        del self.loop_variables[variable]
                else:
                    output.append("Invalid FOR statement")
            elif tokens[0] == "WHILE":
                if len(tokens) >= 4:
                    variable = tokens[1]
                    operator = tokens[2]
                    value = int(tokens[3])
                    if variable in self.variables:
                        current_value = self.variables[variable].balance if variable != "PASSWORD" else self.variables[variable].password_hash
                        while operator == "==" and str(current_value) == value:
                            output.extend(self.interpret(' '.join(tokens[4:])))
                            current_value = self.variables[variable].balance if variable != "PASSWORD" else self.variables[variable].password_hash
                    else:
                        output.append("Variable not found in WHILE statement")
                else:
                    output.append("Invalid WHILE statement")
            elif tokens[0] == "FOREACH":
                if len(tokens) >= 3:
                    variable = tokens[1]
                    collection = tokens[2]
                    if collection == "ACCOUNTS":
                        for acc in self.variables:
                            self.loop_variables[variable] = acc
                            output.extend(self.interpret(' '.join(tokens[3:])))
                    else:
                        output.append("Invalid collection in FOREACH statement")
                else:
                    output.append("Invalid FOREACH statement")
            # Add more operations here
            else:
                output.append("Invalid statement")
        return '\n'.join(output)

# Example usage:
interpreter = BankLangInterpreter()
code = """
CREATE Alice secretpassword 1000;
BALANCE Alice;
FOR i 1 10 1
    FOR a 1 100 1
        DEPOSIT Alice 999;
BALANCE Alice;"""

##############################
# THIS HAS SOME ERRORS IN IT #
# PLEASE FIX BEFORE USING IT #
##############################

print(interpreter.interpret(code))

#print("write '/END/' at the end of every query!")
#if __name__ == "__main__":
#    x = 0
#    while True:
#        query = []
#        code = input(f"{x:<7}|(B3)> ")
#        if "<END>" in code:
#            print("<!> INTERPRETING ...")
#            print(interpreter.interpret(query))
#            code = ""
#        else:
#            query.append(code)
#        x = x + 1 