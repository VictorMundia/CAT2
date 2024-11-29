
from django.db import models
from django.core.validators import MinValueValidator, EmailValidator

class Customer(models.Model):
    """
    Represents a customer in the e-commerce system.
    
    Relationships:
    - One-to-Many relationship with Order model
    - Each customer can have multiple orders
    """
    # Basic customer information fields
    name = models.CharField(
        max_length=200, 
        help_text="Full name of the customer"
    )
    email = models.EmailField(
        unique=True, 
        validators=[EmailValidator()],
        help_text="Unique email address for the customer"
    )
    
    # Additional optional fields for customer profile
    phone_number = models.CharField(
        max_length=15, 
        blank=True, 
        null=True, 
        help_text="Optional customer phone number"
    )
    registered_at = models.DateTimeField(
        auto_now_add=True, 
        help_text="Timestamp of customer registration"
    )

    def __str__(self):
        """
        String representation of the Customer model.
        Returns the customer's name.
        """
        return self.name

class Order(models.Model):
    """
    Represents an order in the e-commerce system.
    
    Relationships:
    - Many-to-One relationship with Customer model
    - Each order is associated with exactly one customer
    """
    # Relationship field with Customer
    customer = models.ForeignKey(
        Customer, 
        on_delete=models.CASCADE,
        related_name='orders',
        help_text="Customer who placed the order"
    )
    
    # Order-specific fields
    order_date = models.DateTimeField(
        auto_now_add=True, 
        help_text="Timestamp when the order was created"
    )
    total_amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Total order amount in decimal format"
    )
    
    # Optional status tracking
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]
    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='pending',
        help_text="Current status of the order"
    )

    def __str__(self):
        """
        String representation of the Order model.
        Returns a descriptive string with order ID and customer name.
        """
        return f"Order {self.id} by {self.customer.name}"