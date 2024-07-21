import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TicTacToeApp(App):
    def build(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False

        layout = GridLayout(cols=3)
        for row in range(3):
            for col in range(3):
                button = Button(text='', font_size=89,
                                on_press=lambda instance, r=row, c=col: self.button_pressed(r, c))
                layout.add_widget(button)
                self.board[row][col] = button

        return layout

    def button_pressed(self, row, col):
        if self.game_over or self.board[row][col].text != '':
            return

        self.board[row][col].text = self.current_player
        if self.check_winner():
            self.game_over = True
            print(f'Player {self.current_player} wins!')
            return

        if self.check_draw():
            self.game_over = True
            print('It\'s a draw!')
            return

        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        # Check rows
        for row in range(3):
            if all(self.board[row][col].text == self.current_player for col in range(3)):
                return True

        # Check columns
        for col in range(3):
            if all(self.board[row][col].text == self.current_player for row in range(3)):
                return True

        # Check diagonals
        if (self.board[0][0].text == self.current_player and self.board[1][1].text == self.current_player and self.board[2][2].text == self.current_player) or \
           (self.board[0][2].text == self.current_player and self.board[1][1].text == self.current_player and self.board[2][0].text == self.current_player):
            return True

        return False

    def check_draw(self):
        return all(self.board[row][col].text != '' for row in range(3) for col in range(3))

if __name__ == '__main__':
    TicTacToeApp().run()
