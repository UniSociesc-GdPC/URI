#2520 - O Último Analógimôn
while(True):
  try:
    n, m = map(int, input().split())
    matrix = []
    posi1 = []
    posi2 = []
    for i in range(n):
      matrix.append(input().split())

    for i in range(n):
      for j in range(m):
        if int(matrix[i][j]) != 0:
          if int(matrix[i][j]) ==1:
            posi1.append(i)
            posi1.append(j)
          else:
            posi2.append(i)
            posi2.append(j)
    valor = abs(posi1[0] - posi2[0]) + abs(posi1[1] - posi2[1])
    print(valor)
  except EOFError:
    break