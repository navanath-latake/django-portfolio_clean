from django.contrib import admin
from .models import Skill, Project, Experience, Contact


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'category', 'order')
    list_filter = ('category',)
    search_fields = ('name',)
    ordering = ('order',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'order', 'created_at')
    list_filter = ('featured', 'created_at')
    search_fields = ('title', 'tech_stack')
    ordering = ('order', '-created_at')


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'duration', 'order')
    search_fields = ('company', 'role')
    ordering = ('order',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'submitted_at', 'is_read')
    list_filter = ('is_read', 'submitted_at')
    search_fields = ('name', 'email')
    ordering = ('-submitted_at',)