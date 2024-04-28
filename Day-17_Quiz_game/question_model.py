class Question:
    def __init__(self, b_text, b_answer):
        self.text = b_text  # self.attribute_name
        self.answer = b_answer
    # And if we want to create an attribute, we have to use this syntax,'self.attribute_name'
    # ,because eventually when we create a new object from this class say a new question object,
    # then we're going to be passing in these two items,


# creating an object 'new_q'

new_q = Question("What the fuk?", "says sara tendulkar")
print(new_q.text)
print(new_q.answer)
