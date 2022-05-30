from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Order(models.Model):
    user_name = models.CharField(max_length=30)
    user_phone_number = PhoneNumberField(null=False, blank=False)
    user_email = models.EmailField()
    order_info = models.TextField(max_length=300)
    oficial_code = models.CharField(max_length=10)
    code = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order by {self.user_name} on time {self.date.strftime("%Y-%m-%d")}'


class Service(models.Model):
    name_of_service = models.CharField(max_length=30)
    description_of_service = models.TextField(max_length=300)
    image_for_service = models.ImageField()

    def __str__(self):
        return f'{self.name_of_service} service'


class Branch(models.Model):
    name_of_branch = models.CharField(max_length=30)
    description_of_branch = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name_of_branch} branch'


class Staff(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name} in {self.branch} branch'


class Offer(models.Model):
    name_of_offer = models.CharField(max_length=30)
    description_of_offer = models.TextField(max_length=300)
    image_of_offer = models.ImageField()

    def __str__(self):
        return f'{self.name_of_offer} offer'


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    content_of_feedback = models.TextField(max_length=300)

    def __str__(self):
        return f'{self.name} feedback'


class Happy_Customer(models.Model):
    name_of_customer = models.CharField(max_length=30)
    job_of_customer = models.CharField(max_length=30)
    message_of_customer = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name_of_customer} (Happy customer)'


class Why_choose_us(models.Model):
    title = models.CharField(max_length=30)
    descriptions = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.title} (why choose us)'


class Contact_us(models.Model):
    email = models.EmailField()
    phone_number = PhoneNumberField()

    def __str__(self):
        return f'Email: {self.email}\nPhone number: {self.phone_number}'


class About_us(models.Model):
    text = models.TextField(max_length=500)


class Logistics_solution(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name} solution'
