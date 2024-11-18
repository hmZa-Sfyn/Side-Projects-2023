import json
import os

def insert(table_name, data):
    table_file = f"{table_name}.json"
    if os.path.exists(table_file):
        with open(table_file, 'r') as f:
            table_data = json.load(f)
    else:
        table_data = []
    
    max_id = max([record['id'] for record in table_data], default=0)
    data['id'] = max_id + 1
    table_data.append(data)
    
    with open(table_file, 'w') as f:
        json.dump(table_data, f, indent=2)

def read(table_name, record_id=None):
    table_file = f"{table_name}.json"
    if os.path.exists(table_file):
        with open(table_file, 'r') as f:
            table_data = json.load(f)
        if record_id is not None:
            for record in table_data:
                if record['id'] == record_id:
                    return record
            return None
        else:
            return table_data
    else:
        return []

def update(table_name, record_id, data):
    table_file = f"{table_name}.json"
    if os.path.exists(table_file):
        with open(table_file, 'r') as f:
            table_data = json.load(f)
        for record in table_data:
            if record['id'] == record_id:
                record.update(data)
                break
        with open(table_file, 'w') as f:
            json.dump(table_data, f, indent=2)
    else:
        print(f"Table {table_name} does not exist.")

def delete(table_name, record_id):
    table_file = f"{table_name}.json"
    if os.path.exists(table_file):
        with open(table_file, 'r') as f:
            table_data = json.load(f)
        new_table_data = [record for record in table_data if record['id'] != record_id]
        with open(table_file, 'w') as f:
            json.dump(new_table_data, f, indent=2)
    else:
        print(f"Table {table_name} does not exist.")

def parse(code):
    lines = code.split('\n')
    for line in lines:
        parts = line.strip().split(' ')
        if parts[0] == 'insert':
            table_name = parts[1]
            try:
                data = json.loads(' '.join(parts[2:]))
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON data for 'insert {table_name}': {e}")
                continue
            insert(table_name, data)
        elif parts[0] == 'read':
            table_name = parts[1]
            record_id = int(parts[2]) if len(parts) > 2 else None
            print(read(table_name, record_id))
        elif parts[0] == 'update':
            table_name = parts[1]
            record_id = int(parts[2])
            data = json.loads('{' + ' '.join(parts[3:]) + '}')
            update(table_name, record_id, data)
        elif parts[0] == 'delete':
            table_name = parts[1]
            record_id = int(parts[2])
            delete(table_name, record_id)
        else:
            print(f"Unknown command: {parts[0]}")

if __name__ == '__main__':
    # Example usage
    code = """
    insert users {"name": "John Doe", "email": "john@example.com"}
    insert users {"name": "Jane Smith", "email": "jane@example.com"}
    insert customers {"name": "ABC Inc.", "contact": "555-1234"}
    insert customers {"name": "XYZ Ltd.", "contact": "555-5678"}
    read users
    read customers
    update users 1 {"email": "johnd@example.com"}
    delete customers 2
    """
    parse(code)