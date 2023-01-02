extends KinematicBody2D

var x : int
var y : int
var velocity = Vector2(100,100)

var lifetime = 10

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

func _physics_process(delta):
	position += velocity * delta
	lifetime -= delta
	if lifetime <= 0:
		queue_free()
