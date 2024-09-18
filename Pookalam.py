from turtle import * 
import math

def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def find_triangle_height_and_base(a, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    h = a * math.sin(theta_radians)
    b = 2 * math.sqrt(a**2 - h**2)
    return h, b
def calculate_arc_dimensions(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    width = 2 * radius * math.sin(angle_radians / 2)
    height = radius - radius * math.cos(angle_radians / 2)
    return width, height
def calculate_arc_radius_and_angle(width, height):
    half_width = width / 2
    radius = math.sqrt(half_width**2 + height**2)
    angle_rad = 2 * math.atan(half_width / height)
    angle_deg = math.degrees(angle_rad)
    return radius, angle_deg
def draw_pentagon(x, y, side_length,pen_down=False,fillclr=None):
		penup()
		angle = 360 / 6
		h,a = find_triangle_height_and_base(side_length,angle)
		goto(x-side_length/2, y-a)
		if pen_down:pendown()
		
		if fillclr is not None:
				fillcolor(fillclr)
				begin_fill()
		for _ in range(5):
			forward(side_length)
			left(angle)
		if fillclr is not None:end_fill()
def draw_eye(x,y,major,minor,fillclr=None,pen_down=True):
	goto(x,y)
	penup()
	x_diff,_ = calculate_arc_dimensions(minor,90)
	penup()
	left(45)
	forward(major*0.02)
	y_center = pos()[1]
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		# circle(major,90)
		chead = heading()
		forward(major*0.02)
		left(60)
		forward(major*0.02)
		setheading(chead+90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_dual_circle(x,y,rad,gap,fillclr,upper_size=3):
  penup()
  goto(x,y-rad-gap)
  setheading(0)
  fillcolor(fillclr)
  begin_fill()
  circle(rad-gap)
  end_fill()
  right(90)
  forward(gap)
  setheading(0)
  color(fillclr)
  pensize(upper_size)
  pendown()
  circle(rad)
  penup()
  color('#000')
def draw_dashed_circle(x,y,rad,fillclr,peaces=10):
  penup()
  goto(x,y-rad)
  setheading(0)
  fillcolor(fillclr)
  for i in range(1,peaces+1):
    if i%2 == 0:
      cx1,cy1 = pos()
      circle(rad,360/peaces)
      cx2,cy2 = pos()
      chead = heading()
      circle(rad,-360/peaces)
      begin_fill()
      circle(rad,360/peaces)
      goto(x,y)
      goto(cx1,cy1)
      end_fill()
      goto(cx2,cy2)
      setheading(chead)
    else:circle(rad,360/peaces)
def draw_theyyam_face(x,y,height):

	eye_pos = height * 0.22
	mouth_pos = height * 0.10
	head_design_pos = height * 0.309
	top_band_pos = height * 0.516
	top_band_height = height * 0.098
	top_band_radius = height * 0.32
	top_band_angle = 95
	penup()
	
	crown_height = height * 0.5
	crown_bottom_width = height * 0.94
	crown_top_circle_gap = height * 0.05
	crown_top_circle_penta_gap = height * 0.1
	goto(x - (crown_bottom_width/2),y+crown_height)
	setheading(90)
	fillcolor('#A01005')
	begin_fill()
	circle(-crown_bottom_width/2,180)
	end_fill()

	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap)),y+crown_height)
	setheading(90)
	num_peaces = 40
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)
		dot(height*0.02,'#fff')
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap)),180/num_peaces/2)

	goto(x - ((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),y+crown_height)
	setheading(90)
	num_peaces = 4
	for _ in range(num_peaces):
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
		chead = heading()
		setheading(0)
		cx,cy = pos()
		draw_pentagon(cx,cy,height*0.082,fillclr='#FC8505')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.053,fillclr='#FEA901')
		setheading(chead)
		goto(cx,cy)
		setheading(0)
		draw_pentagon(cx,cy,height*0.037,fillclr='#D51510')
		setheading(chead)
		goto(cx,cy)
		circle(-((crown_bottom_width/2)-(crown_top_circle_gap+crown_top_circle_penta_gap)),180/num_peaces/2)
	setheading(0)

	draw_dashed_circle(x,y+crown_height+crown_bottom_width/50,crown_bottom_width/5,'#FCF9FB',50)

	face_bottom_circle_ang = 152
	goto(x,y)
	circle(height*0.2196,-face_bottom_circle_ang/2)
	chead = heading()
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	setheading(90)
	forward(top_band_pos - height * 0.16)
	setheading(270)
	fillcolor('#EB5928')
	begin_fill()
	forward(top_band_pos- height * 0.16)
	setheading(chead)
	circle(height*0.2196,face_bottom_circle_ang)
	setheading(90)
	forward(top_band_pos - height * 0.16)
	end_fill()

	goto(tmp_x1+height*0.005,tmp_y1+height*0.035)
	setheading(chead)
	num_peaces = 9
	for i in range(1,num_peaces):
		j = i if i < num_peaces/2 else num_peaces - i
		crad = (height*0.017) * ((2/num_peaces)*(j%(num_peaces/2)))
		circle(height*0.2196 - height * 0.005,face_bottom_circle_ang/num_peaces)
		tmp_x1,tmp_y1 = pos()
		chead = heading()
		draw_dual_circle(tmp_x1,tmp_y1,crad,gap=crad/2.3,fillclr='#A21300',upper_size=height*0.003)
		setheading(chead)
		goto(tmp_x1,tmp_y1)
	

	goto(x,y+top_band_pos)
	setheading(0)
	pendown()
	circle(-top_band_radius,-top_band_angle/2)
	dec_tmp_x1,dec_tmp_y1 = pos()
	dec_tmp_head1 = heading()
	fillcolor('#7F080C')
	begin_fill()
	circle(-top_band_radius,top_band_angle)
	band_tmp_ang = heading()
	band_circle_pos_x,band_circle_pos_y = pos()
	setheading(90)
	forward(top_band_height)
	setheading(band_tmp_ang+180)
	circle(top_band_radius,top_band_angle)
	setheading(270)
	forward(top_band_height)
	band_circle_pos_x1,band_circle_pos_y1 = pos()
	end_fill()
	band_side_circle_rad = height*0.085
	penup()

	goto(dec_tmp_x1,dec_tmp_y1- height * 0.02)
	setheading(dec_tmp_head1)
	num_dots = 50
	for _ in range(num_dots):
		dot(height*0.005,'#FFf')
		circle(-top_band_radius,top_band_angle/num_dots)

	for i in range(1,3):
		goto(dec_tmp_x1,dec_tmp_y1 + ((top_band_height/3)*i))
		setheading(dec_tmp_head1)
		num_dots = 20
		for _ in range(num_dots):
			dot(height*0.02,'#FF9002')
			circle(-top_band_radius,top_band_angle/num_dots)
	

	goto(band_circle_pos_x1,band_circle_pos_y1+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()

	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)

	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.02,'#FF9002')

	goto(band_circle_pos_x,band_circle_pos_y+(band_side_circle_rad - top_band_height))
	setheading(0)
	fillcolor('#6E1109')
	begin_fill()
	circle(band_side_circle_rad)
	end_fill()
	setheading(90)
	forward(height*0.054)
	setheading(0)
	fillcolor('#EB5928')
	begin_fill()
	circle(band_side_circle_rad - height*0.054)
	end_fill()
	setheading(270)
	forward(height * 0.027)
	setheading(0)
	num_dots = 13
	for _ in range(num_dots):
		circle((band_side_circle_rad - height * 0.027),360/num_dots)
		dot(height*0.024,'#FF9002')
	

	goto(x,y+mouth_pos)
	setheading(0)
	lip_bottom_rad = height * 0.087
	lip_bottom_ang = 93
	fillcolor('#A60F06')
	circle(lip_bottom_rad,-lip_bottom_ang/2)
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	begin_fill()
	circle(lip_bottom_rad,lip_bottom_ang)
	tmp_x2,tmp_y2 = pos()
	chead2 = heading()
	end_fill()
	fillcolor('#7C0808')
	goto(tmp_x1,tmp_y1)
	setheading(360-chead)
	begin_fill()
	circle(-lip_bottom_rad/2,lip_bottom_ang)
	end_fill()
	goto(tmp_x2,tmp_y2)
	setheading(360-chead2)
	begin_fill()
	circle(-lip_bottom_rad/2,-lip_bottom_ang)
	end_fill()
	
	eye_gap = height * 0.121
	eye_bottom_rad = 	height * 0.101
	eye_bottom_angle = 114
	eye_eye_gap = height * 0.046
	eye_right_cir_rad = height * 0.075
	eye_right_cir_ang = 106
	goto(x-eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,-eye_bottom_angle/2)
	chead = heading()
	left(80)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,eye_bottom_angle)
	left(110)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(-eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x-eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x-eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x-eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()

	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')

	goto(x+eye_gap,y+eye_pos)
	setheading(0)
	circle(eye_bottom_rad,eye_bottom_angle/2)
	chead = heading()
	left(100)
	circle(-eye_right_cir_rad,eye_right_cir_ang)
	color('pink')
	fillcolor('#382030')
	begin_fill()
	left(180)
	circle(eye_right_cir_rad,eye_right_cir_ang)
	setheading(chead)
	tmp_x1,tmp_y1 = pos()
	tmp_head = heading()
	circle(eye_bottom_rad,-eye_bottom_angle)
	left(70)
	eye_left_cir_rad = height * 0.1793
	eye_left_cir_ang = 42
	circle(eye_left_cir_rad,eye_left_cir_ang)
	end_fill()
	setheading(0)
	draw_eye(x+eye_gap,tmp_y1,height*0.03,height*0.06,fillclr='#fff',pen_down=False)
	goto(x+eye_gap,tmp_y1-height*0.015)
	setheading(0)
	fillcolor('#5A3137')
	begin_fill()
	circle(height*0.015)
	end_fill()
	goto(x+eye_gap,tmp_y1-height*0.005)
	setheading(0)
	fillcolor('#EEE5E6')
	begin_fill()
	circle(height*0.005)
	end_fill()

	setheading(tmp_head)
	goto(tmp_x1,tmp_y1-height * 0.02)
	num_peaces = 10
	for _ in range(num_peaces):
		circle(eye_bottom_rad,-eye_bottom_angle/num_peaces)
		dot(height * 0.009,'#fff')
	nose_gap = height * 0.184
	goto(x,y+nose_gap)
	setheading(90)
	pensize(height*0.02)
	pendown()
	color('#9E1205')
	forward(height* 0.081)
	penup()
	angle_top_circles = 95
	top_circles_mul_gap = height * 0.025
	top_circles_gap = height * 0.364

	goto(x,y+top_circles_gap)
	fillcolor('#9E1205')
	setheading(0)
	circle(-height * 0.1,-angle_top_circles/2)
	tmp_x1,tmp_y1 = pos()
	chead2 = heading() 
	begin_fill()
	chead1 = heading()
	circle(-height * 0.1,angle_top_circles)
	chead = heading() 
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1+height*0.01,angle_top_circles)
	end_fill()

	setheading(chead1)
	left(90)
	forward(height*0.067)
	right(90)
	begin_fill()
	circle(-(height * 0.1 + height*0.067),angle_top_circles)
	chead = heading()
	left(90)
	forward(height*0.01)
	setheading(chead+180)
	circle(height * 0.1 + height*0.067 + height * 0.01,angle_top_circles)
	end_fill()
	

	goto(tmp_x1,tmp_y1)
	setheading(chead2)
	fillcolor('#fff')
	begin_fill()
	circle(-height * 0.1,angle_top_circles)
	end_fill()
	setheading(chead2)
	goto(tmp_x1,tmp_y1)
	left(90)
	forward(height*0.05)
	right(90)
	num_peaces = 20
	for _ in range(num_peaces-1):
		circle(-(height * 0.1 + height*0.05),angle_top_circles/num_peaces)
		dot(height * 0.005,'#fff')
	
def colored_star(x,y,size=40,fillclr=None,angle=120,pen_down=False):
	penup()
	chead = heading()
	goto(x,y)
	setheading(60)
	angle = 120
	forward(size)
	x_diff1,y_len1 = pos()
	backward(size)
	for _ in range(2):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	forward(size)
	right(angle)
	y_diff,y_len2 = pos()
	height = y_len2 - y_len1
	x_diff = x_diff1 - x
	goto(x+x_diff,y_len1+(height/2))
	x1,y1 = pos()
	x_diff = x - x1
	y_diff = y - y1
	goto(x+x_diff,y+y_diff)
	setheading(60)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(5):
		forward(size)
		right(angle)
		forward(size)
		right(72 - angle)
	if fillclr is not None:
		end_fill()
	goto(x,y)
	setheading(chead)
def draw_ellipse(x,y,major,minor,fillclr=None,pen_down=True):
	penup()
	x_diff,y_diff = calculate_arc_dimensions(minor,90)
	y_center = y + (major / 2) - y_diff
	x_center = x + (x_diff /2)
	goto(x_center,y_center)#-major)
	setheading(45)
	if pen_down:pendown()
	if fillclr is not None:
		fillcolor(fillclr)
		begin_fill()
	for _ in range(2):
		circle(major,90)
		circle(minor,90)
	if fillclr is not None:end_fill()
def draw_square(x,y,width,height,angle=0,clr="black",fill=False,border=1,border_clr="black"):
	penup()
	goto(x,y)
	if border > 0:pendown()
	setheading(angle)
	color(border_clr)
	pensize(border)
	if fill:
		fillcolor(clr)
		begin_fill()
	forward(width/2)
	left(90)
	forward(height)
	left(90)
	forward(width)
	left(90)
	forward(height)
	left(90)
	forward(width/2)
	if fill:end_fill()

def draw_theyyam(x,y,width):
	penup()
	setheading(0)
	
	non_circle_len = width * 0.20
	len_square_bottom = width * 0.137
	len_half_circle = width * 0.5
	
	height = non_circle_len + len_square_bottom+len_half_circle#width * 0.67
	y = y - height /2
	
	goto(x-width/2,y)
	left(90)
	forward(len_square_bottom+non_circle_len)
	fillcolor("#720B26")
	begin_fill()
	circle(-len_half_circle,180) # top circle
	end_fill()
	fillcolor('#D7140E')
	
	half_circle_gap = width * 0.093
	penup()
	
	setheading(90)
	goto(x-width/2+half_circle_gap,y+(len_square_bottom+non_circle_len))
	begin_fill()
	
	circle(-len_half_circle + half_circle_gap,180)
	end_fill()
	
	setheading(90)
	goto(x-width/2+half_circle_gap*2,y+(len_square_bottom+non_circle_len))
	fillcolor('#FF5C01')
	begin_fill()
	
	circle(-len_half_circle + half_circle_gap*2,180)
	end_fill()
	goto(x-(width/2)+(half_circle_gap/2),y+(len_square_bottom+non_circle_len)) # design position
	setheading(90)
	num_dots = 32
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap/2),180/num_dots)
		dot(width*0.024,'#FF9002')
	goto(x-width/2+half_circle_gap+(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap+(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	goto(x-width/2+(half_circle_gap*2)-(width * 0.015),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 64
	for _ in range(num_dots - 1):
		circle(-len_half_circle + ((half_circle_gap*2)-(width*0.015)),180/num_dots)
		dot(1.5,'#FFF')
	goto(x-width/2+(half_circle_gap*1.5),y+(len_square_bottom+non_circle_len))
	setheading(90)
	num_dots = 11
	for _ in range(num_dots - 1):
		circle(-len_half_circle + (half_circle_gap*1.5),180/num_dots)
		cx,cy = pos()
		colored_star(cx,cy,size=width*0.01,fillclr="#FFF")
	center_no_circle_rad = width * 0.19 
	center_mul_circle_gap = width * (0.061 - 0.006) 
	for i  in range(3):
		goto(x-center_no_circle_rad-(center_mul_circle_gap*i),y+(len_square_bottom+non_circle_len))
		setheading(90)
		num_dots = 30 + (i * 10)
		for _ in range(num_dots - 1):
			circle(-(center_no_circle_rad+(center_mul_circle_gap*i)),180/num_dots)
			dot(width*0.012,'#FF9002')
	draw_square(x,y+non_circle_len,width,len_square_bottom,fill=True,clr='#FF5C01',border=0) 
	draw_square(x,y+non_circle_len + (width * 0.024),width - (width * 0.015),len_square_bottom - 2*(width * 0.024),fill=True,clr='#720B26',border=0) # bottom_square

	setheading(0)
	goto(x-width/2,y+non_circle_len + (width * 0.012))
	num_peaces = 50
	for _ in range(num_peaces - 1):
		forward(width / num_peaces)
		dot(width*0.012,'#FF9002')
	goto(x-width/2,y+non_circle_len + len_square_bottom - (width * 0.012))
	for _ in range(num_peaces - 1):
		forward(width / num_peaces)
		dot(width*0.012,'#FF9002')
	
	goto(x-(width - (width * 0.015))/2,y+non_circle_len + (width * 0.024) + (len_square_bottom - 2*(width * 0.024))/2)
	setheading(0)
	wi_btm = width - (width * 0.015)
	num_peaces = 8
	for i in range(num_peaces):
		forward(wi_btm/num_peaces/2)
		dot(width * 0.028,'#FE3000')
		setheading(270)
		forward(width *0.031)
		num = 20
		setheading(0)
		for _ in range(num):
			dot(width*0.005,'#FC9103')
			circle(width * 0.031,360/num)
		setheading(90)
		forward(width *0.031)
		setheading(0)
		forward(wi_btm/num_peaces/2)


	bottom_len = width / 2 
	bottom_one_height = width * 0.1
	bottom_band_height = width * 0.115 
	bottom_band_ang = 90 
	bottom_r2 = width * 0.17 / 2
	penup()

	setheading(270)
	goto(x - (bottom_len/4),y+(non_circle_len))
	fillcolor('#A01005')
	begin_fill()
	forward(non_circle_len - bottom_band_height)
	left(90)
	forward(bottom_len/2)
	left(90)
	forward(non_circle_len - bottom_band_height)
	end_fill()

	setheading(0)
	goto(x - (bottom_len/2),y+(non_circle_len)+len_square_bottom)
	right(90)

	fillcolor('#F53F10')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	circle(bottom_r2,180)
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	tmp_cir_x1,tmp_cir_y1 = pos()
	end_fill()

	setheading(270)
	goto(x + (bottom_len/2),y+(non_circle_len)+len_square_bottom)
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	circle(-bottom_r2,180)
	forward(bottom_one_height - bottom_r2+len_square_bottom)
	tmp_cir_x2,tmp_cir_y2 = pos()
	end_fill()

	setheading(0)
	goto(x - (bottom_len/2) + (width * 0.02),y+(non_circle_len)+len_square_bottom)
	right(90)
	fillcolor('#D7140E')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	circle(bottom_r2 - (width * 0.02),90)
	tmp_x1,tmp_y1 = pos() 
	circle(bottom_r2 - (width * 0.02),90)
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	end_fill()
	setheading(0)
	goto(tmp_x1,tmp_y1+width * 0.03/2)
	val_for_cir = tmp_cir_x1 - (x - (bottom_len/2) + (width * 0.02)) - width * 0.03
	fillcolor('#FE9102')
	begin_fill()
	circle(val_for_cir/2)
	end_fill()
	goto(tmp_x1,tmp_y1+width * 0.03)
	setheading(0)
	num_peaces = 20
	for _ in range(num_peaces):
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
		dot(width*0.012,'#F83201')
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
	goto(tmp_x1,tmp_y1+width * 0.105)
	setheading(0)
	fillcolor('#7C0808')
	begin_fill()
	circle(val_for_cir/2- width * 0.09)
	end_fill()

	setheading(0)
	goto(x + (bottom_len/2) - (width * 0.02),y+(non_circle_len)+len_square_bottom)
	right(90)
	fillcolor('#D7140E')
	begin_fill()
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	circle(-(bottom_r2 - (width * 0.02)),90)
	tmp_x1,tmp_y1 = pos() 
	circle(-(bottom_r2 - (width * 0.02)),90)
	forward(bottom_one_height - bottom_r2+len_square_bottom - (width * 0.01))
	end_fill()
	setheading(0)
	goto(tmp_x1,tmp_y1+width * 0.03/2)
	val_for_cir = tmp_cir_x1 - (x - (bottom_len/2) + (width * 0.02)) - width * 0.03
	fillcolor('#FE9102')
	begin_fill()
	circle(val_for_cir/2)
	end_fill()
	goto(tmp_x1,tmp_y1+width * 0.03)
	setheading(0)
	num_peaces = 20
	for _ in range(num_peaces):
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
		dot(width*0.012,'#F83201')
		circle(val_for_cir/2- width * 0.03/2,360/num_peaces/2)
	goto(tmp_x1,tmp_y1+width * 0.105)
	setheading(0)
	fillcolor('#7C0808')
	begin_fill()
	circle(val_for_cir/2- width * 0.09)
	end_fill()

	draw_square(x,y+(non_circle_len)+(len_square_bottom/2),bottom_len,len_square_bottom/2,fill=True,border=0,clr='#9B9698')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01),bottom_len-(width*0.036*1),len_square_bottom/2-(width*0.01),fill=True,border=0,clr='#A6AAAB')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01*2),bottom_len-(width*0.036*2),len_square_bottom/2-(width*0.01*2),fill=True,border=0,clr='#B5B7B9')
	draw_square(x,y+(non_circle_len)+(len_square_bottom/2)+(width*0.01*3),bottom_len-(width*0.036*3),len_square_bottom/2-(width*0.01*3),fill=True,border=0,clr='#EDEDEF')

	r = bottom_len / 2
	penup()
	setheading(0)
	goto(x,y)
	fillcolor('#7C0808')
	right(180)
	circle(-r,bottom_band_ang/2)
	begin_fill()
	right(180)
	circle(r,bottom_band_ang)
	tmp_x2, tmp_y2 = pos()
	cur_head = heading()
	setheading(90)
	forward(bottom_band_height)
	setheading(cur_head+180)
	tmp_x1,tmp_y1 = pos()
	chead = heading()
	circle(-r,bottom_band_ang)
	setheading(270)
	forward(bottom_band_height)
	end_fill()
	goto(tmp_x1,tmp_y1-(width * 0.02))
	setheading(chead)
	num_peaces = 28
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		dot(width * 0.01,'#fff')
	goto(tmp_x2,tmp_y2+(width * 0.02))
	setheading(chead)
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		dot(width * 0.01,'#fff')
	goto(tmp_x2,tmp_y2+(bottom_band_height/2))
	setheading(chead)
	num_peaces = 8
	for _ in range(num_peaces-1):
		circle(-r,bottom_band_ang/num_peaces)
		cx,cy = pos()
		chead = heading()
		draw_dashed_circle(cx,cy,width*0.02,'#FF5C01',20)
		goto(cx,cy)
		setheading(chead)
	setheading(0)
	draw_theyyam_face(x,y+bottom_band_height,width * 0.455)
	return height
	
def reset_position(x=0,y=0):
   setheading(0)
   goto(x,y)

def draw_squash(rad,num_rows,len_row,num_peaces,colors):
  left(90)
  penup()
  initial = rad - (num_rows*len_row)
  forward(rad - initial)
  right(90)
  pendown()
  ang = 360 / num_peaces
  counter = 0
  right(90)
  for j in range(0,num_rows):
    for i in range(0,num_peaces):
        penup()
        fillcolor(colors[counter % len(colors)])
        begin_fill()
        left(90)
        circle(initial+(len_row*j),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(-(initial+len_row+(len_row*j)),ang)
        right(90)
        forward(len_row)
        right(90)
        circle(initial+(len_row*j),ang)
        right(90)
        end_fill()
        counter += 1
    forward(len_row)
  return rad - initial
def draw_circular(rad,rad_len,sub_circle_count=3,colors=['red','green','blue'],num_peaces = 20,pen_down = True):
  x,y = pos()
  penup()
  vis_len = rad_len * 1
  second_rad_diff = rad_len / sub_circle_count
  ruler_circle_rad = rad - rad_len * 2
  ruler_ang = 360 / num_peaces
  circle(rad)
  for j in range(0,int(num_peaces)):
    for i in range(0,sub_circle_count):
      left(90)
      forward((second_rad_diff if i != 0 else 0 ))
      right(90)
      fillcolor(colors[i % len(colors)])
      begin_fill()
      if pen_down:pendown()
      circle(rad_len - (second_rad_diff * i))
      penup()
      end_fill()
    right(90)
    forward(rad_len-second_rad_diff)
    left(90)
    circle(rad,ruler_ang) 
  reset_position(x,y)
  left(180)
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) 
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle((rad_len - second_rad_diff),180) 
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[1])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) 
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  if pen_down:pendown()
  circle(rad_len-second_rad_diff,180)
  end_fill()
  left(90)
  penup()
  forward(second_rad_diff)
  left(90)
  fillcolor(colors[2])
  begin_fill()
  if pen_down:pendown()
  circle(-(rad_len - (second_rad_diff * 2)),180) 
  end_fill()
  penup()
  reset_position(x,y)
  circle(rad,ruler_ang) 
  left(180)
  fillcolor(colors[0])
  begin_fill()
  if pen_down:pendown()
  circle(-rad_len,180) 
  right(90)
  penup()
  forward(second_rad_diff)
  right(90)
  if pen_down:pendown()
  circle(rad_len - second_rad_diff,180) 
  end_fill()
  penup()
  reset_position(x,y+rad_len)
  fillcolor('#014504')
  begin_fill()
  circle(rad-vis_len)
  end_fill()
  return vis_len




rad = 400 


setup(1000,1000)
title("Code A Pookalam - Reuben Sam Philip")
tracer(0,0) 
update()
# speed(0) 

penup() 
reset_position(0,-rad)
x,y = pos()
def circ(len,clr):
    penup()
    home()
    goto(0, -(len+0))
    pendown()
    color(clr)
    begin_fill()
    circle(len)
    end_fill()


circ(401,"#3d0706")


num_rows = 8 
len_row = 10 
num_peaces = 35 
colors = ["#3d0706","#cf342b","#fcd349","#F06D0A",'#FACA27','#EDE9DE']
circular_width = 50
cut_threshold = 1.6

colors2 = ['#ba3035','#BB5C08','#DEC727','#cf342b']

occ_circular = draw_circular(rad,circular_width,colors=colors2,num_peaces=int(((rad)*math.pi*2)/(circular_width*cut_threshold)),sub_circle_count=4,pen_down=False)
reset_position(0,y=y+occ_circular) 
padding_circle = 5
fillcolor('#021322')
begin_fill()
circle(rad-occ_circular)
end_fill()
new_rad = rad-occ_circular - padding_circle 
reset_position(y=y+occ_circular+padding_circle)
occ_squash = draw_squash(new_rad,num_rows,len_row,num_peaces,colors)  

reset_position(0,y+occ_squash+padding_circle+occ_circular+5)
fillcolor('#014504')
begin_fill()
circle(rad - occ_squash-padding_circle-occ_circular-5)
end_fill()

draw_dashed_circle(0,0,rad - occ_squash-padding_circle-occ_circular-5,fillclr='#f2eecd',peaces=20)

th_height = draw_theyyam(0,rad*0.1,(rad-occ_squash-padding_circle-occ_circular-20)*2)

goto(0,0 - th_height/2 - ((rad-occ_squash-padding_circle-occ_circular-20)- th_height/2) / 2)

width,height = screensize()
penup()
goto(width - 20,-rad+15)
setheading(270)
color('black')
pendown()
write("- Reuben Sam Philip",align="right",font=("Arial", 7, "normal"))
penup()
forward(15)
color('#800B05')
pendown()
write("\"Code A Pookalam\"",align="right",font=("Arial", 8, "bold"))
penup()

mainloop()
