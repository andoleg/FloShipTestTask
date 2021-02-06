from djchoices import DjangoChoices, ChoiceItem


class OrderStatus(DjangoChoices):
    new = ChoiceItem('New')
    in_progress = ChoiceItem('In progress')
    stored = ChoiceItem('Stored')
    sent = ChoiceItem('Sent')

