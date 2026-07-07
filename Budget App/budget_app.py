class Category:
    #Initialisation
    def __init__(self, category):
        self.category = str(category)
        self.amount = 0
        self.ledger = []
        self.withdrawn = 0

    #Deposit
    def deposit(self, amount, description = ''):
        self.amount += amount
        self.ledger.append({'amount': round(amount, 2), 'description': description})

    #check balance
    def check_funds(self, amount):
        if amount <= self.amount:
            return True
        elif amount > self.amount:
            return False

    #Withdraw
    def withdraw(self, amount, description = '', yes_no = True):
        if self.check_funds(amount):
            if yes_no is True:
                self.withdrawn += amount
            self.deposit(-amount, description)
            return True
        else:
            return False
    
    #get balance
    def get_balance(self):
        return round(self.amount, 2)

    #transfer
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.category, False)
            category.deposit(amount, 'Transfer from ' + self.category)
            return True
        else:
            return False  

    #Print
    def __str__(self):
        #title line
        title_line = self.category.center(30, '*')

        #body
        body = ''
        for expense in self.ledger:
            body += expense['description'][:23].ljust(23) + ('%.2f' % expense['amount']).rjust(7) + '\n'

        #final output
        return title_line + '\n' + body + 'Total: ' + str(self.get_balance())

def create_spend_chart(categories):
    #checking length
    if len(categories) <= 4:
        #total spending and name
        total_spending = 0
        name_tally = []
        for category in categories:
            total_spending += category.withdrawn
            name_tally.append(len(category.category))

        #defining lines
        lines = ['  0| ', ' 10| ', ' 20| ', ' 30| ', ' 40| ', ' 50| ', ' 60| ', ' 70| ', ' 80| ', ' 90| ', '100| ']
        dashed_line = '    -'

        #percentage spending
        percentage = None
        for category in categories:
            percentage = int(((category.withdrawn / total_spending)*100)//10 * 10)
            for i in range(len(lines)):
                if (i*10) <= percentage:
                    lines[i] += 'o  '
                else:
                    lines[i] += '   '
            dashed_line += '---'        

        #bar graph
        bar_graph = ''
        for i in range(len(lines)):
            bar_graph = lines[i] + '\n' + bar_graph
        bar_graph.strip()

        #name tally
        category_name = ''
        for i in range(max(name_tally)):
            category_name += '     '
            for category in categories:
                try:
                    category_name += category.category[i] + '  '
                except:
                    category_name += '   '
            category_name += '\n'

    #final output
    return 'Percentage spent by category\n' + bar_graph + dashed_line + '\n' + category_name.rstrip('\n')
