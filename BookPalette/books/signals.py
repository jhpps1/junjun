from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import UserBookRelation
from accounts.models import User

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(*rgb)

def calc_user_profile_color_mixed(user):
    relations = UserBookRelation.objects.filter(user=user)
    if not relations.exists():
        return "#CCCCCC"
    weights = {'like': 1, 'read': 2}
    total_weight = 0
    sum_r = sum_g = sum_b = 0
    for rel in relations:
        color = rel.book.category.color
        r, g, b = hex_to_rgb(color)
        weight = weights.get(rel.status, 1)
        sum_r += r * weight
        sum_g += g * weight
        sum_b += b * weight
        total_weight += weight
    avg_r = int(sum_r / total_weight)
    avg_g = int(sum_g / total_weight)
    avg_b = int(sum_b / total_weight)
    return rgb_to_hex((avg_r, avg_g, avg_b))

@receiver(post_save, sender=UserBookRelation)
@receiver(post_delete, sender=UserBookRelation)
def update_user_profile_color(sender, instance, **kwargs):
    user = instance.user
    color = calc_user_profile_color_mixed(user)
    user.profile_color = color
    user.save(update_fields=["profile_color"])
