from stretching.models import *
from stretching.database import db_session 



# for q in housingQs:
# 	Q = Question()
# 	Q.Text = q
# 	Q.Category_id = 3
# 	db_session.add(Q)

db_session.commit()