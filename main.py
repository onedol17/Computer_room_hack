#1. 음식은 2 개씩 묶음으로 주어진다.
#2. 음식을 2 조각 먹은 개체는 다음날까지 생존하고 자기 자신을 복제할 수 있다.
#3. 호전적인 비둘기파끼리 만나면 먹이를 1/2씩 나누어 먹습니다.
#4. 공격적인 매파끼리 만난다면 싸우면서 시간을 낭비해서 다음날 살아남지 못합니다.
#5. 매파와 비둘기파끼리 만나면 매파는 1.5개의 먹이를 먹어 살아남을 확률은 100% 번식 확률은 50%이고 0.5개의 먹이를 먹은 비둘기파는 다음날 50%의 확률로 살아남습니다.
import random

# 초기 설정
rounds = 10
hawks = [1, 1, 1, 1]
doves = [1, 1, 1, 1]
food_per_day = 100  # 하루에 주어지는 음식 묶음 수

def simulate_day(hawks, doves, food_per_day, rounds):

    null = food_per_day
    if food_per_day < (len(hawks)+len(doves)):
        null = (2 * food_per_day) - (len(hawks)+len(doves))
    
    # 현재 생존하는 개체 리스트
    organisms = ['hawk'] * len(hawks) + ['dove'] * len(doves) + ["null"] * food_per_day
    random.shuffle(organisms)

    # 음식 묶음 생성
    food = [2] * food_per_day
    

    # 짝짓기 및 상호작용 시뮬레이션
    while food and len(organisms) >= 2:
        org1 = organisms.pop()
        org2 = organisms.pop()
        
        if org1 == 'hawk' and org2 == 'hawk':
            # 두 매파가 만나면 둘 다 생존하지 못함
            hawks.pop()
            hawks.pop()
            food.pop()
            
        elif org1 == 'dove' and org2 == 'dove':
            # 두 비둘기파가 만나면 각각 1개씩 먹이를 나눠 먹음

            food.pop()  # 음식 하나 소모
        # 매파와 비둘기파가 만나면 매파가 1.5개, 비둘기파가 0.5개 먹음
        elif org1 == 'hawk' and org2 == 'dove':
            food.pop()
            if random.random() > 0.5:
                hawks.append(1)
            if random.random() > 0.5:
                doves.pop()

        elif org1 == 'dove' and org2 == 'hawk':
            food.pop()
            if random.random() > 0.5:
                hawks.append(1)
            if random.random() > 0.5:
                doves.pop()

        elif org1 == 'null' and org2 == 'null':
            rounds += 1

        elif org1 == 'null' and org2 != 'null':
            food.pop()
            if org2 == "hawk":
                hawks.append(1)
            elif org2 == "dove":
                doves.append(1)

        elif org2 == 'null' and org1 != 'null':
            food.pop()
            if org1 == "hawk":
                hawks.append(1)
            elif org1 == "dove":
                doves.append(1)
        
       

    return hawks, doves

# 시뮬레이션 실행
for p in range(rounds):
    hawks, doves = simulate_day(hawks, doves, food_per_day, rounds)
    print(f"Round {p + 1}: Hawks = {len(hawks)}, Doves = {len(doves)}")

print(f"Final Population: Hawks = {len(hawks)}, Doves = {len(doves)}")
 
