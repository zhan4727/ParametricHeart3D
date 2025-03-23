from manim import *

class Heart3D(ThreeDScene):
	def construct(self):
		# set camera orientation
		self.set_camera_orientation(phi=75 * DEGREES, theta=65 * DEGREES)
		
		# define parametric equations
		def heart_parametric(u,v):
			x = 15*np.sin(u)-4*np.sin(3*u)*np.sin(v)
			y = 8*np.cos(v)
			z = np.sin(v)*(15*np.cos(u)-5*np.cos(2*u)-2*np.cos(3*u)-np.cos(4*u))
			return np.array([x,y,z])

		# Create the heart surface
		heart = Surface(
			heart_parametric,
			u_range = [0, 2*PI],
			v_range = [0, PI],
			resolution = (50, 50),
			checkerboard_colors = False
		).scale(0.2).shift(OUT*3)
		heart.set_fill(RED, opacity=0.5)

		# animate the heart creation
		self.play(Create(heart), run_time = 3)

		# Rotate the heart
		self.begin_ambient_camera_rotation(rate=0.35)
		self.wait(10)