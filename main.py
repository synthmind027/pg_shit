import pg
import time


if __name__ == '__main__':
	pg.init()
	pg.font.init()
	fnt = pg.font.Font('D2.ttf', 15)
	srf_main = pg.display.set_mode((0,0))
	flag_run = True
	while flag_run:
		for e in pg.event.get():
			if e.type == pg.QUIT:
				flag_run = False
			elif e.type == pg.MOUSEMOTION:
				e = e.pos
			elif e.type == pg.KEYDOWN:
				e = e.scancode
			elif e.type == pg.KEYUP:
				e = e.scancode
			elif e.type == pg.MOUSEWHEEL:
				e = (e.precise_x, e.precise_y)
			elif e.type == pg.MOUSEBUTTONDOWN:
				e = e.button
			elif e.type == pg.MOUSEBUTTONUP:
				e = e.button

		srf_main.fill((0,0,0))
		srf_txt = fnt.render('wow!@#', True, (255,255,255))
		srf_main.blit(srf_txt, (20,20))
		pg.display.flip()
	pg.font.quit()
	pg.quit()
