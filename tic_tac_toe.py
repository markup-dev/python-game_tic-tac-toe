from datetime import datetime


def check_winner(area):
	# Проверка всех возможных выигрышных комбинаций
	winning_combinations = [
		# Горизонтальные
		[area[0][0], area[0][1], area[0][2]],
		[area[1][0], area[1][1], area[1][2]],
		[area[2][0], area[2][1], area[2][2]],
		# Вертикальные
		[area[0][0], area[1][0], area[2][0]],
		[area[0][1], area[1][1], area[2][1]],
		[area[0][2], area[1][2], area[2][2]],
		# Диагонали
		[area[0][0], area[1][1], area[2][2]],
		[area[0][2], area[1][1], area[2][0]]
	]

	for combination in winning_combinations:
		if combination == ['X', 'X', 'X']:
			return 'X'
		elif combination == ['0', '0', '0']:
			return '0'

	return None  # Ничья или игра продолжается


def show_statistics():
	try:
		with open('statistics.txt', 'r', encoding='utf-8') as f:
			print(f.read())
	except FileNotFoundError:
		print("Статистика еще не записана.")


def draw_area(area):
	for row in area:
		print(' '.join(row))
	print()


def main():
	area = [['*'] * 3 for _ in range(3)]
	users = {}
	winner = None

	print("Добро пожаловать в крестики-нолики")
	print("----------------------------------")

	if input('Показать статистику? (y/n) ').lower() == 'y':
		show_statistics()

	users['X'] = [input('Введите имя 1-го игрока (X): '), 'X']
	users['0'] = [input('Введите имя 2-го игрока (0): '), '0']
	print(f'-------------------------------------\n')

	draw_area(area)

	start_time = datetime.now()

	for turn in range(9):
		current_char = 'X' if turn % 2 == 0 else '0'
		current_user = users[current_char]

		print(f'Ходят {current_char}, {current_user[0]}')

		while True:
			try:
				row = int(input('Введите номер строки (1, 2, 3): ')) - 1
				column = int(input('Введите номер столбца (1, 2, 3): ')) - 1
				print('-------------------------------------')

				if 0 <= row <= 2 and 0 <= column <= 2:
					if area[row][column] == '*':
						area[row][column] = current_char
						break
					else:
						print('Ячейка уже занята, попробуйте снова.')
				else:
					print('Неправильный ввод, попробуйте снова.')
			except ValueError:
				print('Пожалуйста, введите число.')

		draw_area(area)

		winner = check_winner(area)
		if winner:
			print('-------------------------------------')
			print(f'Победа {winner}, поздравляем - {current_user[0]}')
			break
	else:
		print('-------------------------------------')
		print('Ничья')

	end_time = datetime.now()

	with open('statistics.txt', 'a', encoding='utf-8') as f:
		f.write(
			f'Итог: \n{users["X"][0]} vs {users["0"][0]}\n'
			f'Победитель - {users[winner][0] if winner else "Ничья"}\n'
			f'Длительность партии - {end_time - start_time}\n\n'
		)

	if input('Показать статистику? (y/n) ').lower() == 'y':
		print()
		show_statistics()


if __name__ == "__main__":
	main()
