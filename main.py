import pg
import time

if __name__ == '__main__':
	char_map = '''`1234567890-=~!@#$%^&*()_+qwertyuiop[]\\QWERTYUIOP{}|asdfghjkl;'ASDFGHJKL:"zxcvbnm,./ZXCVBNM<>?'''

	# [INIT] initializing phase
	pg.init()
	pg.font.init()
	fnt = pg.font.Font('D2.ttf', 15)
	srf_main = pg.display.set_mode((0,0))
	pg.mouse.set_visible(False)


	flag_run = True
	ts = time.time()
	curr = dict()
	curr['e'] = dict()
	curr['m_pos'] = (0,0)
	curr['e']['m_mo'] = list()
	curr['e']['m_wh'] = list()
	curr['e']['m_dn'] = list()
	curr['e']['m_up'] = list()
	curr['e']['k_dn'] = list()
	curr['e']['k_up'] = list()
	curr['trail'] = dict()
	curr['trail']['past'] = (0,0)
	curr['trail']['curr'] = (0,0)
	curr['trail']['thre'] = 10
	curr['trail']['sz'] = 5
	while flag_run:
		ts = time.time()
	

		curr['e']['m_mo'] = []
		curr['e']['m_wh'] = []
		curr['e']['m_dn'] = []
		curr['e']['m_up'] = []
		curr['e']['k_dn'] = []
		curr['e']['k_up'] = []


		# [GAT] Event gathering sector
		while True:
			e = pg.event.poll()
			if e.type == pg.NOEVENT:
				break
			if e.type == pg.QUIT:
				flag_run = False
			elif e.type == pg.MOUSEMOTION:
				curr['e']['m_mo'].append(e.pos)
				curr['m_pos'] = e.pos
			elif e.type == pg.KEYDOWN:
				curr['e']['k_dn'].append(e.scancode)
			elif e.type == pg.KEYUP:
				curr['e']['k_up'].append(e.scancode)
			elif e.type == pg.MOUSEWHEEL:
				curr['e']['m_wh'].append((e.precise_x, e.precise_y))
			elif e.type == pg.MOUSEBUTTONDOWN:
				curr['e']['m_dn'].append(e.button)
			elif e.type == pg.MOUSEBUTTONUP:
				curr['e']['m_up'].append(e.button)


		# [APP] Event applying sector

		# [APP] Escape
		if 41 in curr['e']['k_dn']:
			flag_run = False


		# [APP] Calculate mouse trail
		# curr [trail] [vec / pnts / ts / adopt]
		curr['trail']['past'] = curr['trail']['curr']
		curr['trail']['curr'] = curr['m_pos']





		# [DRA] Drawing sector

		# [DRA] General
		srf_main.fill((0,0,0))
		srf_txt = fnt.render('wow', True, (255,255,255))
		srf_main.blit(srf_txt, (20,20)),

		# [DRA] Trail
		t_c = curr['trail']['curr']
		t_p = curr['trail']['past']
		t_t = curr['trail']['thre']
		t_s = curr['trail']['sz']
		d = ( (t_c[0] - t_p[0]) ** 2 + (t_c[1] - t_p[1]) ** 2 ) ** 0.5
		if d > t_t:
			n = int(d / t_t) + 2
			norm = [0,0]
			norm[0] = (t_c[0] - t_p[0]) / d
			norm[1] = (t_c[1] - t_p[1]) / d
			perp = [-norm[1],norm[0]]
			for i in range(1, n):
				p = [0, 0]
				p[0] = t_c[0] * (i/n) + t_p[0] * (1-i/n)
				p[1] = t_c[1] * (i/n) + t_p[1] * (1-i/n)
				q = [0, 0]
				q[0] = p[0] - t_s * norm[0] + t_s * perp[0]
				q[1] = p[1] - t_s * norm[1] + t_s * perp[1]
				pg.draw.aaline(srf_main, (255,255,255), p, q)
				q = [0, 0]
				q[0] = p[0] - t_s * norm[0] - t_s * perp[0]
				q[1] = p[1] - t_s * norm[1] - t_s * perp[1]
				pg.draw.aaline(srf_main, (255,255,255), p, q)
		#pg.draw.aaline(srf_main, (255,255,255), curr['trail']['curr'], curr['trail']['past'])

		# [DRA] Cursor
		pg.draw.rect(srf_main, (255,255,255), (curr['m_pos'],(5,5)))
		pg.display.flip()

		time.sleep(max(0,1/pg.FPS - (time.time() - ts)))
