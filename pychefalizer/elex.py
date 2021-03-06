# English to Chef lexer
# -*- coding: utf8 -*-

import lex
from ply.lex import TOKEN

# Matches a word character
WC = b'(?P<S>[A-Za-z\'])'
# Matches a new word
NW = b'(?P<S>[^A-Za-z\'])'

class Elex(lex.Lex):
	# Whether we have seen the letter 'i' in the current word
	seen_i = False


	def iw(self, token, a):
		token.value = a
		token.lexer.begin('inw')
		return self.s(token)

	def mc(self, source, replacement):
		if len(source) == 0 or len(replacement) == 0:
			return ""

		out = ""
		i = 0
		j = len(source) - 1

		for c in replacement:
			if source[i].isupper():
				out += c.upper()
			else:
				out += c.lower()

			if i < j:
				i += 1

		return out

	def cw(self, token, replacement):
		token.lexer.begin('inw')
		token.value = self.mc(token.value, replacement)
		return self.s(token)

	def s(self, token):
		m = token.lexer.lexmatch.groupdict()
		if 'S' in m and m['S'] is not None:
			token.value += m['S']
		return token

	def nop(self, token):
		token.lexer.begin('inw')
		return token


	states = (
		('inw', 'inclusive'),
		('niw', 'inclusive')
	)

	def t_inw_error(self, token):
		token.lexer.skip(1)

	def t_niw_error(self, token):
		token.lexer.skip(1)

	tokens = [
		'newline', 'nroff',
		'NOTWORD', 'DOBORK', 'BORK',
		'AN', 'AU', 'A', 'EN', 'EW',
		'E_NW', 'E', 'F', 'IR', 'I',
		'OW', 'O', 'THE', 'TH', 'TION',
		'U', 'V', 'W',
		'DOT'
	]

	@TOKEN(b'[.!?]$')
	def t_DOBORK(self, token):
		token.lexer.begin('niw')
		token.lexer.lineno += len(token.value)
		self.seen_i = False
		token.value = ". Bork bork bork" + token.value
		return token

	# Define a rule so we can track line numbers
	@TOKEN(b'\\n+')
	def t_newline(self, token):
		token.lexer.begin("niw")
		token.lexer.lineno += len(token.value)
		self.seen_i = False
		return token

	# Ignore obvious groff/nroff directives
	@TOKEN(b'^\.[A-Za-z0-9][A-Za-z0-9]')
	def t_nroff(self, token):
		token.lexer.begin("niw")
		return token


	@TOKEN(NW)
	def t_NOTWORD(self, token):
		token.lexer.begin('niw')
		return token

	@TOKEN(b'[Bb]ork' + NW)
	def t_niw_BORK(self, token):
		return token

	@TOKEN(b'[Aa]n' + WC)
	def t_AN(self, token):
		return self.cw(token, 'un')

	@TOKEN(b'[Aa]u' + WC)
	def t_AU(self, token):
		return self.cw(token, 'po')

	@TOKEN(b'[Aa]' + WC)
	def t_A(self, token):
		return self.cw(token, 'e')

	@TOKEN(b'en' + NW)
	def t_EN(self, token):
		return self.iw(token, 'en')

	@TOKEN(b'ew')
	def t_inw_EW(self, token):
		return self.iw(token, 'oo')

	@TOKEN(b'e' + NW)
	def t_inw_E_NW(self, token):
		return self.iw(token, 'e-a')

	@TOKEN(b'[Ee]')
	def t_niw_E(self, token):
		return self.cw(token, 'i')

	@TOKEN(b'f')
	def t_inw_F(self, token):
		return self.iw(token, 'ff')

	@TOKEN(b'ir')
	def t_inw_IR(self, token):
		return self.iw(token, 'ur')

	@TOKEN(b'i')
	def t_inw_I(self, token):
		if self.seen_i:
			return self.iw(token, 'i')
		else:
			self.seen_i = True
			return self.iw(token, 'ee')

	@TOKEN(b'ow')
	def t_inw_OW(self, token):
		return self.iw(token, 'oo')

	@TOKEN(b'[Oo]')
	def t_niw_O(self, token):
		return self.cw(token, 'oo')

	@TOKEN(b'o')
	def t_inw_O(self, token):
		return self.iw(token, 'u')

	@TOKEN(b'[Tt]he')
	def t_THE(self, token):
		return self.cw(token, 'zee')

	@TOKEN(b'th' + NW)
	def t_TH(self, token):
		return self.iw(token, 't')

	@TOKEN(b'tion')
	def t_inw_TION(self, token):
		return self.iw(token, 'shun')

	@TOKEN(b'[Uu]')
	def t_inw_U(self, token):
		return self.cw(token, 'oo')

	@TOKEN(b'[Vv]')
	def t_V(self, token):
		return self.cw(token, 'f')

	@TOKEN(b'[Ww]')
	def t_W(self, token):
		return self.cw(token, 'v')

	@TOKEN(b'.')
	def t_DOT(self, token):
		return self.nop(token)

