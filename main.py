from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.lang import Builder


class MainApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.solution = TextInput(multiline=False, readonly=True, halign="right", font_size=55)
        self.solution.text = '0'
        self.first_num = ''
        self.second_num = ''
        self.operation = ''
        mainLayout = BoxLayout(orientation='vertical')
        mainLayout.add_widget(self.solution)
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', 'C', '+'],
        ]
        for lis in buttons:
            h_layout = BoxLayout()
            for pos in lis:
                button = Button(text=pos)
                button.bind(on_press=self.btn_pressed)
                h_layout.add_widget(button)
            mainLayout.add_widget(h_layout)

        ravno_btn = Button(text='=')
        ravno_btn.bind(on_press=self.on_solution)
        mainLayout.add_widget(ravno_btn)
        return mainLayout

    def btn_pressed(self, instance):
        button_text = instance.text
        if button_text in self.operators:
            if self.first_num == '':
                self.first_num = '0'
                self.operation = button_text
                self.solution.text = ''
            elif self.first_num != '' and self.operation != '' and self.second_num != '':
                if self.operation == '+':
                    if self.second_num != '': #Эта ветка для того, что бы когда я делаю 3 + 3 и еще + 3 что бы числа скалыдвались
                        result = float(self.first_num) + float(self.second_num)
                        if int(result) == result:
                            self.solution.text = str(int(result))
                        else:
                            self.solution.text = str(result)
                        self.first_num = self.solution.text
                        self.second_num = ''
                        self.operation = button_text
                    else:
                        result = float(self.first_num) + float(self.second_num)
                        if int(result) == result:
                            self.solution.text = str(int(result))
                        else:
                            self.solution.text = str(result)
                        self.first_num = self.solution.text
                        self.second_num = ''
                        self.operation = ''
            else:
                self.operation = button_text
                return
        elif button_text == 'C':
            if self.second_num == '' and self.operation == '':
                self.solution.text = '0'
                self.first_num = ''
            elif self.first_num != '' and self.operation != '':
                self.solution.text = '0'
                self.second_num = ''
            else:
                return
        elif button_text not in self.operators:
            if self.operation == '':
                self.first_num = self.first_num + button_text
                self.solution.text = self.first_num
            else:
                self.second_num = self.second_num + button_text
                self.solution.text = self.second_num

        print('first_num = ', self.first_num)
        print('oper = ', self.operation)
        print('second_num = ', self.second_num)

    def on_solution(self, instance):
        #print('Мы тут')
        #print('Мы тут')
        if self.operation == '+':
            result = float(self.first_num) + float(self.second_num)
            if int(result) == result:
                self.solution.text = str(int(result))
            else:
                self.solution.text = str(result)
            self.first_num = self.solution.text
            self.second_num = ''
            self.operation = ''
        elif self.operation == '-':
            pass
        elif self.operation == '*':
            pass
        elif self.operation == '/':
            pass
        else:
            return

        #print('first_num = ', self.first_num)
        #print('oper = ', self.operation)
        #print('second_num = ', self.second_num)


if __name__ == '__main__':
    app = MainApp()
    app.run()