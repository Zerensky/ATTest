from datetime import datetime
import json

class Note:
    head: str
    body: str
    date: str

    def __init__(self, head, body):
        self.head = head
        self.body = body
        self.date = datetime.now().replace(microsecond=0)

    def classoutput(self):
        return [self.head, self.body, self.date]


class NotebookFileOperation:
    def __init__(self):
        pass

    def open_file(self) -> dict:
        file = open("notebook.csv", 'r')
        notes = {}
        for line in file:
            notes[line.split(';')[0]] = [line.split(';')[1], line.split(';')[2], line.split(';')[3][:-1]]
        file.close()
        return notes

    def write_file(self, notes: dict):
        file = open("notebook.csv", 'w')
        counter = 1
        for value in notes.values():
            file.write(f'{counter};{value[0]};{value[1]};{value[2]}\n')
            counter += 1
        file.close()

    def save_json(self):
        file = open("notebook.csv", 'r')
        notes = {}
        for line in file:
            n = line.split(';')
            notes[n[0]] = {'Head': n[1], 'Body' : n[2], 'Date': n[3]}
        with open('json_file.json', 'w') as f:
            json.dump(notes, f)


class NotebookEditor:

    def __init__(self):
        self.fileOperator = NotebookFileOperation()
    
    def get_all_notes(self):
        notes = self.fileOperator.open_file()
        return notes
    
    def add_note(self, note: Note):
        notes = self.fileOperator.open_file()
        id = len(notes.keys()) + 1
        notes[id] = note.classoutput()
        self.fileOperator.write_file(notes)

    def edit_note(self, id: str, note: Note):
        notes = self.fileOperator.open_file()
        for key in notes.keys():
            if key == id:
                notes[key] = note.classoutput()
        self.fileOperator.write_file(notes)
            
    def delete_note(self, id: str):
        notes = self.fileOperator.open_file()
        for key in notes.keys():
            if key == id:
                notes.pop(key)
                break
        self.fileOperator.write_file(notes)

    def sort_notes(self, date: datetime):
        notes = self.fileOperator.open_file()
        datas = []
        for val in notes.values():
            datas.append(val[2])
        new_data = datetime.strftime(date, '%Y-%m-%d')
        sorted_notes = {}
        for key, value in notes.items():
            if new_data in value[2]:
                sorted_notes[key] = value
        return sorted_notes


            

