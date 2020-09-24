"""admin.py"""
from django.contrib import admin
from django.utils.html import format_html
from .models import Team, Player, Matches

# Register your models here.


@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    """team of admin page"""
    @classmethod
    def image_tag(cls, obj):
        """image tag"""
        return format_html(
            '<img src="{}" height="20" width="20"/>'.format(
                obj.logo_url.url
            )
        )
    image_tag.short_description = 'Image'
    list_display = ('image_tag', 'name')


@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    """players of admin page"""
    @classmethod
    def image_tag(cls, obj):
        """image tag"""
        return format_html(
            '<img src="{}" height="20" width="20"/>'.format(
                obj.image_url.url
            )
        )
    image_tag.short_description = 'Image'
    list_display = ('image_tag', 'firstname', 'lastname')


@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    """matches of admin page"""
    list_display = ('left_team', 'right_team', 'winner_team')
    readonly_fields = ('left_team', 'right_team', 'winner_team')
