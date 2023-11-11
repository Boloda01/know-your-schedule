"""
Copyright (c) 2023 qdiaps

Програмне забеспечення поширюється з ліцензією MIT.
Детальніше дивіться у файлі LICENSE.
"""
default_days = ['1. Понеділок', '2. Вівторок', '3. Середа', '4. Четверг', '5. П\'ятниця', '6. Субота']


def delete_schedule(school_name, class_name, day, obj):
  if school_name in obj and class_name in obj[school_name] and day in obj[school_name][class_name]:
      del obj[school_name][class_name][day]


def delete_class(school_name, class_name, obj):
  if school_name in obj and class_name in obj[school_name]:
      del obj[school_name][class_name]


def delete_school(school_name, obj):
  if school_name in obj:
      del obj[school_name]

def edit_schedule():
	pass

def edit_class():
	pass

def edit_school():
	pass

def add_new_schedule(school_name, class_name, day, schedules, obj):
   if school_name in obj:
      if class_name in obj[school_name]:
         obj[school_name][class_name][day] = schedules

def add_new_class(school_name, class_name, obj):
   if school_name in obj:
      if class_name not in obj:
         obj[school_name][class_name] = {}
         for day in default_days:
            obj[school_name][class_name][day] = []

def add_new_school(school_name, obj):
   if school_name not in obj:
      obj[school_name] = {}