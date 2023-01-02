extends Node


onready var projectile = load("res://scenes/projectile.tscn")

func read_input():
	if Input.is_action_just_pressed("debug_spawnProjectile"):
		print(get_viewport().get_mouse_position())
		var instance = projectile.instance()
		instance.set_position(get_viewport().get_mouse_position())
		add_child(instance)
		
		
func _physics_process(delta):
	read_input()
