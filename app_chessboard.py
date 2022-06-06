from tkinter import *


def repaint():
    for y in matrix_buttons:
        for x in y:
            even_columns = y.index(x) % 2
            odd_columns = not even_columns
            even_row = matrix_buttons.index(y) % 2
            odd_row = not even_row
            if even_columns and odd_row or odd_columns and even_row:
                x['background'] = 'DarkRed'
            elif even_columns and even_row or odd_columns and odd_row:
                x['background'] = 'Yellow'


def paint_horizontal():
    repaint()
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            if y == row_number and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif y == row_number and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_vertical():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            if x == column_number and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif x == column_number and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_cell():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            if cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'


def paint_rook():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            horizontal_vertical = x == column_number or y == row_number
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif horizontal_vertical and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif horizontal_vertical and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_diagonal_main():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            main_diagonal = x - column_number == y - row_number
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif main_diagonal and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif main_diagonal and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_diagonal_second():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            second_diagonal = len_row - x + column_number == y + len_row - row_number
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif second_diagonal and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif second_diagonal and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_elephant():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            main_diagonal = x - column_number == y - row_number
            second_diagonal = len_row - x + column_number == y + len_row - row_number
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif (main_diagonal or second_diagonal) and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif (main_diagonal or second_diagonal) and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_queen():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            horizontal_vertical = x == column_number or y == row_number
            main_diagonal = x - column_number == y - row_number
            second_diagonal = len_row - x + column_number == y + len_row - row_number
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif (horizontal_vertical or main_diagonal or second_diagonal) and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif (horizontal_vertical or main_diagonal or second_diagonal) and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_three_horizontal():
    repaint()
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            three_horizontal = row_number - 1 <= y <= row_number + 1
            if three_horizontal and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif three_horizontal and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_three_vertical():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            three_vertical = column_number - 1 <= x <= column_number + 1
            if three_vertical and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif three_vertical and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_king():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            three_vertical = column_number - 1 <= x <= column_number + 1
            three_horizontal = row_number - 1 <= y <= row_number + 1
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif three_vertical and three_horizontal and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif three_vertical and three_horizontal and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


def paint_hoarse():
    repaint()
    column_number = top_cells.index(entry_cell.get().upper()[0]) - 1
    row_number = len(matrix_buttons) - int(entry_cell.get()[1])
    for y in range(len(matrix_buttons)):
        len_row = len(matrix_buttons[y])
        for x in range(len_row):
            color_dark = x % 2 and not y % 2 or not x % 2 and y % 2
            color_bright = x % 2 and y % 2 or not x % 2 and not y % 2
            cell_center = x == column_number and y == row_number
            bottom_and_top_x = x == column_number - 1 or x == column_number + 1
            bottom_and_top_y = y == row_number - 2 or y == row_number + 2
            left_and_right_x = x == column_number - 2 or x == column_number + 2
            left_and_right_y = y == row_number - 1 or y == row_number + 1
            if cell_center and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkBlue'
            elif cell_center and color_bright:
                matrix_buttons[y][x]['background'] = 'Blue'
            elif bottom_and_top_x and bottom_and_top_y or left_and_right_x and left_and_right_y and color_dark:
                matrix_buttons[y][x]['background'] = 'DarkGreen'
            elif bottom_and_top_x and bottom_and_top_y or left_and_right_x and left_and_right_y and color_bright:
                matrix_buttons[y][x]['background'] = 'Green'


app = Tk()
app.title('Chess board')

top_cells = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', '']

matrix_buttons = []
for row, _ in enumerate(top_cells):
    matrix_temp = []
    matrix_buttons.append(matrix_temp)
    for column, char in enumerate(top_cells):
        row_condition = row == 0 or row == len(top_cells) - 1
        column_condition = column == 0 or column == len(top_cells) - 1
        if row_condition and column_condition:
            Label(background='Yellow', borderwidth=1, relief='solid').grid(column=column, row=row, stick=NSEW)
        elif row_condition:
            Label(text=char, background='Yellow', relief='solid').grid(column=column, row=row, ipady=5, ipadx=25,
                                                                       stick=NSEW)
        elif column_condition:
            text = len(top_cells) - 1 - row
            Label(text=text, background='Yellow', relief='solid').grid(column=column, row=row, ipady=18, ipadx=10,
                                                                       stick=NSEW)
        elif column % 2 == 1 and row % 2 == 1 or column % 2 == 0 and row % 2 == 0:
            button = Button(bg='Yellow')
            matrix_temp.append(button)
            button.grid(column=column, row=row, stick=NSEW)
        elif column % 2 == 0 and row % 2 == 1 or column % 2 == 1 and row % 2 == 0:
            button = Button(bg='DarkRed')
            matrix_temp.append(button)
            button.grid(column=column, row=row, stick=NSEW)

matrix_buttons.pop()
matrix_buttons.pop(0)

frame_right = Frame()
frame_right.grid(column=len(top_cells), row=0, rowspan=10, sticky=NSEW)
Label(frame_right, text='Enter cell:').pack()
entry_cell = Entry(frame_right)
entry_cell.pack()
Button(frame_right, text='Repaint', command=repaint).pack(fill=BOTH, expand=1)
Button(frame_right, text='horizontal', command=paint_horizontal).pack(fill=BOTH, expand=1)
Button(frame_right, text='vertical', command=paint_vertical).pack(fill=BOTH, expand=1)
Button(frame_right, text='cell', command=paint_cell).pack(fill=BOTH, expand=1)
Button(frame_right, text='rook', command=paint_rook).pack(fill=BOTH, expand=1)
Button(frame_right, text='diagonal_main', command=paint_diagonal_main).pack(fill=BOTH, expand=1)
Button(frame_right, text='diagonal_second', command=paint_diagonal_second).pack(fill=BOTH, expand=1)
Button(frame_right, text='elephant', command=paint_elephant).pack(fill=BOTH, expand=1)
Button(frame_right, text='queen', command=paint_queen).pack(fill=BOTH, expand=1)
Button(frame_right, text='three horizontal', command=paint_three_horizontal).pack(fill=BOTH, expand=1)
Button(frame_right, text='three vertical', command=paint_three_vertical).pack(fill=BOTH, expand=1)
Button(frame_right, text='king', command=paint_king).pack(fill=BOTH, expand=1)
Button(frame_right, text='hoarse', command=paint_hoarse).pack(fill=BOTH, expand=1)

app.mainloop()
