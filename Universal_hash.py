gAAAAABfUTzLn7YFa2VP_EqX7zdYLwwpKJd2-eo9ip4l7IjKWwaZM04rkJONTp_FEUIRPOZYx2HWUla9Bk9POPcE3wX3gzU4pOZqBGAS7mdej9GGsbvZecAS-0sel_0ATy4WsfN2ybk7bVO-RS-dDF_CcqglPhX3y6gbqm9tqe9G7fKnU5x_XGCobrdJ1TADt8GkYwVbHbjCEd7pbY6aQqX433P3syIicB13PNUcKdQAO-fTz31kqAvMKUJN8WvJ5Tln2-S_UzAbL4nmv2zAKrHpko7JSWpWEhIX5HQ_GQRI_gUuhPYMJ2VK6lqjtkT-Z_qFLz7LBgX9vnDkzN40YUYfNVW_1jrFOB-qikYMkg-UfVGtaHl52XYhpWJmb3pSh7VWQzGcrNNecbKxHMDLlvbmlFH9Zstu5i5l0fwixG2Fjj63MESkDDloxncM0SgT66VX7FRFi-yVEo6kXXddyPeUG_Sdw1e-vm_Ixk51MiEvWG59Wl2xV-9AODbm0bAP2AgojmLmQ8-xFMkqEHsk33nGS6YCvgmgSFr__U6AcnLcnzUVZ02kZevI78_e8Mop1keFwBNBo8ck6eFqDQMeCzNwKSFBJOhsd-l6PYs9oIEaylzJ4IzN1jshNoapgaaKdf32gVllh7iZ5XZj_04_Otfct4gWoN2XIxWrQ0Cv6hciuQJ-y1WBzFOS0a-SZFMH2KqeXOKiansVJUDgEhMSiL4xVjjZrBbKdPpixP6fq0iZO7jcp2yXfYohyKpFqerHkaH9RvjH0Qyw5ehDH0fnR6Mqu2hIidsasAF50L7Zk3bzzl0tGgcQfEHiSDP062xr3ZTjx4L0piH1vtmwJ-GGZBVvjdhckj6SyO-w_Gxh3tJjC0s1H-iz_4z-VhdUz8rEeTBvCU8CaIDwTxBLEc1WiaW6adlDLws5OuAIbE4q8TrLPjuHcC50YxJQyjz2CqjJns4wqp08lCMzKO2YDlfAnmR_09_v9WuOZrUtsJWR6nDxazREWggXdenwPNw8jmXlP0iM0T1xYpl4tLUOVIeGMi7gM3VJaG58O4CrUsmMO_1bKeIOqvs9TzvR1cl3eBByOezk7qDnWOqASGbF_0CmT7352J1SjHSuYygi2yGw2rqpF59YwOw7yF7JVT3hfhnnkms0HiBKQzl-PQEoFU3mCLl7K-b6D9VHYbnkNw4IPHZBgMHH919oCRvV3MQffOPr0lDR6K3JanZMSJct3-nY093TGj6DKkGM6ji3U4FN1177-bqQG1eSVFYfMq5CteiIWcu5DKsXXWiRufqIIh67p-O0zuuOuCgYFHxabshmlUwAFj62OGI5vWeKm2tWbwSHiAmus5AsjM2TkY-P-2bmG7GfL_dyAIGlVecdxMTg9QiOoBySilIlNXFiBcVWzIkFGtFAH4FjwU6b8adN_ukw82Db5SAwYT9bUSK5YSuE862KrFAhROBoubQ=

import random

class HashTable:

    def __init__(self, size):

        self.size = size
        self.slots = []
        for i in range(self.size):
            self.slots.append([])
        self.func = random.choice(func_list)

    def hash_func(self, value):

        return self.func(value)

    def put(self, value):

        self.slots[self.hash_func(value)].append(value)
        
    def find(self, value):

        flag = 0
        place = ()
        for i in range(len(self.slots)):
            if value in self.slots[i]:
                flag += 1
                place = (i, self.slots[i].index(value))
                break
            else:
                pass
        if flag != 0:
            return value, place
        else:
            return None

func_list = [(lambda value: ((2 * value + 5) % 167) % 17),
             (lambda value: ((3 * value + 7) % 173) % 17),
             (lambda value: ((5 * value + 13) % 179) % 17)]

test = HashTable(17)

for i in range(34):
    test.put(i)
print(test.find(25))
