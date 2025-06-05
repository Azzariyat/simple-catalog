from django.core.management.base import BaseCommand
from catalog.models import Product, ProductFeature

class Command(BaseCommand):
    help = 'Creates sample products for the catalog'

    def handle(self, *args, **kwargs):
        # Clear existing products
        Product.objects.all().delete()

        # Sample products
        products = [
            {
                'name': 'Premium Laptop',
                'description': 'High-performance laptop with the latest processor, 16GB RAM, and 512GB SSD storage. Perfect for both work and gaming.',
                'price': 1299.99,
                'category': 'electronics',
                'features': [
                    '15.6" 4K Display',
                    '16GB RAM',
                    '512GB SSD',
                    'NVIDIA RTX Graphics'
                ]
            },
            {
                'name': 'Wireless Earbuds',
                'description': 'True wireless earbuds with active noise cancellation, premium sound quality, and long battery life.',
                'price': 199.99,
                'category': 'electronics',
                'features': [
                    'Active Noise Cancellation',
                    '24-hour Battery Life',
                    'Water Resistant',
                    'Touch Controls'
                ]
            },
            {
                'name': 'Classic Denim Jacket',
                'description': 'Timeless denim jacket made from premium cotton. Features a comfortable fit and classic styling.',
                'price': 79.99,
                'category': 'clothing',
                'features': [
                    '100% Cotton Denim',
                    'Button Closure',
                    'Multiple Pockets',
                    'Machine Washable'
                ]
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight and comfortable running shoes with advanced cushioning technology.',
                'price': 129.99,
                'category': 'sports',
                'features': [
                    'Breathable Mesh',
                    'Cushioned Sole',
                    'Arch Support',
                    'Available in Multiple Colors'
                ]
            },
            {
                'name': 'Smart Coffee Maker',
                'description': 'WiFi-enabled coffee maker that you can control from your phone. Schedule brewing times and customize your perfect cup.',
                'price': 159.99,
                'category': 'home',
                'features': [
                    'WiFi Connected',
                    '12-cup Capacity',
                    'Programmable Timer',
                    'Keep Warm Function'
                ]
            },
            {
                'name': 'Bestselling Novel',
                'description': 'Award-winning novel that takes you on an unforgettable journey. A must-read for book lovers.',
                'price': 24.99,
                'category': 'books',
                'features': [
                    'Hardcover Edition',
                    'Award Winner',
                    'Includes Bonus Content',
                    'Author-signed Bookplate'
                ]
            }
        ]

        for product_data in products:
            features = product_data.pop('features')
            product = Product.objects.create(**product_data)
            
            for feature in features:
                ProductFeature.objects.create(product=product, feature=feature)

        self.stdout.write(self.style.SUCCESS('Successfully created sample products')) 