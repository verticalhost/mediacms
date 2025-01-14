from .models import User, Badge

def add_points(user, points):
    user.points += points
    user.save()
    check_level_up(user)

def check_level_up(user):
    level_thresholds = [100, 200, 300]  # Example thresholds
    for threshold in level_thresholds:
        if user.points >= threshold and user.level < level_thresholds.index(threshold) + 2:
            user.level = level_thresholds.index(threshold) + 2
            user.save()

def award_badge(user, badge_name):
    badge, created = Badge.objects.get_or_create(name=badge_name)
    user.badges.add(badge)
    user.save()
