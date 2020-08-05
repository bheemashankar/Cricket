from django.contrib import admin
from .models import Team, Player, Matches
from django.utils.html import format_html

# Register your models here.    

@admin.register(Team)
class TeamsAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="20" width="20"/>'.format(obj.logo_url.url))
    image_tag.short_description = 'Image'
    list_display = ('image_tag', 'name')


@admin.register(Player)
class PlayersAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" height="20" width="20"/>'.format(obj.image_url.url))
    image_tag.short_description = 'Image'
    list_display = ('image_tag', 'firstname', 'lastname')
    

@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('left_team', 'right_team', 'winner_team')
    readonly_fields = ('left_team', 'right_team', 'winner_team')

