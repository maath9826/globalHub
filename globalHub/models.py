from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Frieght_Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name_of_branch = models.CharField(max_length=30)
    description_of_branch = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name_of_branch} branch'


class Order(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    user_phone_number = PhoneNumberField(null=False, blank=False)
    user_email = models.EmailField()
    order_info = models.TextField(max_length=300)
    # official_code = models.CharField(max_length=30)
    # code = models.CharField(max_length=6, unique=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Order by {self.user_name} on time {self.date.strftime("%Y-%m-%d")}'


class Service(models.Model):
    name_of_service = models.CharField(max_length=40)
    description_of_service = models.TextField()
    icon_url = models.TextField(default='globalHub/assets/images/Aireplane.svg')
    image_url = models.TextField(default='globalHub/assets/images/Aireplane.svg')
    # tempelate_class = models.TextField(default='')
    # image_for_service = models.ImageField()

    def __str__(self):
        return f'{self.name_of_service} service'


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
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} feedback on {self.date.strftime("%Y-%m-%d")}'


class Why_choose_us(models.Model):
    title = models.CharField(max_length=60)
    descriptions = models.TextField()
    image_url = models.TextField(default="globalHub/assets/images/reason-savetime.png")
    # image = models.ImageField()

    def __str__(self):
        return f'{self.title} (why choose us)'


class Contact_us(models.Model):
    email = models.EmailField()
    phone_number = PhoneNumberField()
    facebook_url = models.TextField(default="")
    instagram_url = models.TextField(default="")
    telegram_url = models.TextField(default="")

    def __str__(self):
        return f'Email: {self.email}\nPhone number: {self.phone_number}'


class About_us(models.Model):
    text = models.TextField()


class Logistics_solution(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name} solution'


class Quote(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = PhoneNumberField()
    freightType = models.ForeignKey(Frieght_Type, on_delete=models.CASCADE)
    departureCity = models.CharField(max_length=30)
    deliveryCite = models.CharField(max_length=30)
    height = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    length = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)

    fragile = models.BooleanField()
    expressDelivery = models.BooleanField()
    insurance = models.BooleanField()
    packaging = models.BooleanField()

    # code = models.CharField(max_length=6, unique=True, null=True)
    # official_Code = models.CharField(max_length=300, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Quote by {self.name} on time {self.date.strftime("%Y-%m-%d")}'


class Contact(models.Model):
    # branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    phone_number = PhoneNumberField(null=False, blank=False)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return f'Contact by {self.name} on time {self.date.strftime("%Y-%m-%d")}'