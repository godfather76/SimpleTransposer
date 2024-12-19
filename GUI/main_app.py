from GUI import qt_classes as qt
import sys

key_dict = {'C -  C,  D,  E,  F,  G,  A,  B': 'c',
            'C#/Db -  Db, Eb, F,  Gb, Ab, Bb, C': 'c#',
            'D -  D,  E,  F#, G,  A,  B,  C#': 'd',
            'D#/Eb -  Eb, F,  G,  Ab, Bb, C,  D': 'd#',
            'E -  E,  F#, G#, A,  B,  C#, D#': 'e',
            'F -  F,  G,  A,  Bb, C,  D,  E': 'f',
            'F#/Gb -  Gb, Ab, Bb, B,  Db, Eb, F': 'f#',
            'G -  G,  A,  B,  C,  D,  E,  F#': 'g',
            'G#/Ab -  Ab, Bb, C,  Db  Eb, F,  G': 'g#',
            'A -  A,  B,  C#, D,  E,  F#, G#': 'a',
            'A#/Bb -  Bb, C,  D,  Eb, F,  G,  A': 'a#',
            'B -  B,  C#, D#, E,  F#, G#, A#': 'b'}

note_num_dict = {'c': 0,
                 'c#': 1,
                 'd': 2,
                 'd#': 3,
                 'e': 4,
                 'f': 5,
                 'f#': 6,
                 'g': 7,
                 'g#': 8,
                 'a': 9,
                 'a#': 10,
                 'b': 11}

transpose_chars = ['#', '+']
note_letters = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
all_notes = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']


def get_dist(from_key, to_key):
    from_key_index = list(note_num_dict.keys()).index(from_key)
    this_note_list = all_notes.copy()
    append_notes = this_note_list[:from_key_index]
    if append_notes:
        del this_note_list[:from_key_index]
        this_note_list += append_notes
    distance1 = this_note_list.index(to_key) - 0
    to_key_index = this_note_list.index(to_key)
    append_notes = this_note_list[:to_key_index]
    if append_notes:
        del this_note_list[:to_key_index]
        this_note_list += append_notes
    distance2 = this_note_list.index(from_key) - 0
    dist = min(distance1, distance2)
    if dist == distance2:
        dist = 0 - dist
    return dist


def transpose(note, dist):
    this_note_list = all_notes.copy()
    if note == 'e#':
        note = 'f'
    elif note == 'b#':
        note = 'c'
    if dist < 0:
        end_piece = this_note_list[this_note_list.index(note) + 1:]
        del this_note_list[this_note_list.index(note) + 1:]
        this_note_list = end_piece + this_note_list
        new_note = this_note_list[11 + dist]
    else:
        begin_piece = this_note_list[:this_note_list.index(note)]
        del this_note_list[:this_note_list.index(note)]
        this_note_list += begin_piece
        new_note = this_note_list[dist]
    return new_note


def parse_line(line, from_key, to_key):
    # make line lowercase for ease
    line = line.lower()
    # new_line will be a string we add things to one at a time
    new_line = ''
    # new_note will be used to determine which branch of the if statement to go into
    new_note = True
    dist = get_dist(from_key, to_key)
    # set cur_val (current value) to blank. This will be used to allow for sharps and upper octaves
    cur_val = ''
    # loop through values in the line
    for i, val in enumerate(line):
        # if it's a new note
        if new_note:
            # if the value is not a letter
            if not val.isalpha():
                # append a question mark to the line.
                new_line += '?'
            # if the value is a letter
            else:
                # if it's not a letter that can represent a note,
                if val not in note_letters:
                    # append a question mark to the line
                    new_line += '?'
                # if the value is in note_letters,
                else:
                    # set cur_val to this val
                    cur_val = val
                    # if this is not the last value in the line,
                    if i != len(line) - 1:
                        # if the next value is a not a letter,
                        if not line[i + 1].isalpha():
                            # set new_note to false, so we go through the second branch
                            new_note = False
                            if line[i + 1] == '#':
                                cur_val += '#'
                                new_line += transpose(cur_val, dist)
                            elif line[i + 1] == '+':
                                new_line += transpose(cur_val, dist)
                        # if the next line is a letter,
                        else:
                            new_line += transpose(cur_val, dist)
                        cur_val = ''
                    else:
                        new_line += transpose(cur_val, dist)

        else:
            if val not in transpose_chars:
                new_line += '?'
                new_note = True
            else:
                if val == '+':
                    new_line += val
                elif val == '#':
                    cur_val = ''
                if i != len(line) - 1:
                    if line[i + 1] != '+':
                        new_note = True
    return new_line


class MainWindow(qt.QtWidgets.QMainWindow):
    def __init__(self, main_app, *args, **kwargs):
        self.main_app = main_app
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Transposer v1!')
        self.resize(400, 200)
        main_widget = MainWidget(self)
        self.setCentralWidget(main_widget)
        file = qt.QtCore.QFile('Darkeum_teal.qss')
        if not file.open(qt.QtCore.QFile.ReadOnly | qt.QtCore.QFile.Text):
            return

        qss = qt.QtCore.QTextStream(file)
        self.setStyleSheet(qss.readAll())
        # self.setWindowFlags(qt.QtCore.Qt.WindowType.FramelessWindowHint)
        # self.title_bar = qt.CustomTitleBar(self)
        self.show()
        sys.exit(self.main_app.exec())


class MainWidget(qt.QtWidgets.QWidget):
    text_box = None
    go_button = None

    def __init__(self, root, *args, **kwargs):
        self.root = root
        super().__init__(*args, **kwargs)
        # self.layout = qt.QtWidgets.QVBoxLayout(self)
        self.layout = qt.QtWidgets.QGridLayout(self)
        gb = qt.GroupBox(self.root, title='Transposer v1', layout=self.layout)
        gblayout = qt.QtWidgets.QVBoxLayout(gb)

        self.from_key_drop = qt.ComboBox(self.root,
                                         layout=gblayout, )
        self.from_key_drop.addItems(list(key_dict.keys()))
        self.to_key_drop = qt.ComboBox(self.root,
                                       layout=gblayout)
        self.to_key_drop.addItems(list(key_dict.keys()))
        self.input = qt.TextEdit(self.root,
                                 placeholderText='Input: Enter or copy and paste the notes here. Use sharps instead of '
                                                 'flats. If you want to add lyrics or comments, on the line above the '
                                                 'notes they go with, put a - followed by the lyrics or comments.',
                                 layout=gblayout)
        self.output = qt.TextEdit(self.root,
                                  layout=gblayout,
                                  readOnly=True,
                                  placeholderText='Output')
        self.go_button = qt.PushButton(self.root,
                                       text='Go!',
                                       layout=gblayout,
                                       func=self.go)
        self.show()

    @qt.QtCore.Slot()
    def go(self):
        from_key = key_dict[self.from_key_drop.currentText()]
        to_key = key_dict[self.to_key_drop.currentText()]
        lines = self.input.toPlainText().split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('-'):
                new_lines.append(line)
            else:
                new_lines.append(parse_line(line, from_key, to_key))
        self.output.setPlainText('\n'.join(new_lines))
