salutation = "приветствие"
name = "название"
product = "продукт"
verbed = "глагол"
room = "комната"
animals = "животные"
amount = "238"
percent = "10"
spokesman = "представитель"
job_title = "название вакансии"

letter = \
    """
    Dear {0} {1}, 
    
    Thank you for your letter. We are sorry that our {2} 
    {3} in your {4}. Please note that it should never 
    be used in a {4}, especially near any {5}. 
    
    Send us your receipt and {6} for shipping and handling. 
    We will send you another {2} that, in our tests, 
    is {7}% less likely to have {3}. 
    
    Thank you for your support. 
    Sincerely, 
    {8} 
    {9}
    """
ltr = letter.format(salutation, name, product, verbed, room, animals, amount, percent, spokesman, job_title)
print(ltr)
