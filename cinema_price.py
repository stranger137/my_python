print("��� ������������ ��������� �������� ��������� ������. ����������, ������� ��������:")
film_name = input()
film_time = 0
ticket_price = 0
sale = 0

if film_name == "1917":
    print("�������� ����� ������: 10, 13 ��� 16 �����")
    film_time = int(input())
    if film_time == 10:
        ticket_price = 250
    else:
        ticket_price = 350
elif film_name == "��������":
    print("�������� ����� ������: 12, 16 ��� 20 �����")
    if film_time == 12:
        ticket_price = 250
    elif ticket_price == 16:
        ticket_price = 350
    elif ticket_price == 16 or ticket_price == 20:
        ticket_price = 450
    else:
        print("������� �������� �����. ��������� �������")
elif film_name == "����� � ����":
    print("�������� ����� ������: 10, 14 ��� 18 �����")
    if film_time == 10:
        ticket_price = 350
    elif film_time == 14 or film_time == 18:
        ticket_price = 450
    else:
        print("������� �������� �����. ��������� �������")
else:
    print("������� �������� ����� ������. ��������� �������")
    
print("����� �� ����������� �������� ����? ������� 0, ���� �������, 1 ���� ������,�� ��������� ���� ������� ����� ������ �����. ���� �� ������� ������, �� ��� ���� ������ 5%!")
date = int(input())
if date == 1:
    sale += 5
print("������� �������� ������� ������ ������ � ����? ���� ������ 20, ��� ���� ������ 20%!")
people = int(input())
if people >= 20:
    sale += 20
    
ans = ticket_price*people*sale/100
print("��������� ��������� �������", ans, "������. ��������� ���������!")
