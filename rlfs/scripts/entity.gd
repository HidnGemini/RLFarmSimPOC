extends KinematicBody2D
class_name Entity

# Variables

var velocity : Vector2 = Vector2()
var direction : Vector2 = Vector2()

var max_hp : int = 5
var current_hp : int = 5

func regen_hp(amount):
	if (current_hp < max_hp):
		if (current_hp + amount > max_hp):
			current_hp = max_hp
		else:
			current_hp += amount

func damage_hp(amount):
	current_hp -= amount
