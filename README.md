# DADS5001_final
1. โหลดโฟลเดอร์ final หรือ git clone repo
2. run Docker
3. เปิด cmd หรือ powershell change work directory ที่โฟลเดอร์ที่เก็บไฟล์ไว้ เช่น เก็บไฟล์ไว้ในโฟลเดอร์ D:\DADS5001 ใช้ `cd D:\DADS5001` หรือ กรณีอยู่คนละไดรฟ์ ใช้ `cd /d D:\DADS5001`
4. เริ่มใช้งาน docker-compose โดยรัน command นี้ `docker-compose up -f final\docker-compose.yml up --build` ใน cmd หรือ powershell โดย final\docker-compose.yml คือที่อยู่ไฟล์ docker-compose.yml 
5. ตอนรันครั้งแรกจะใช้เวลานานหน่อย 2-7 นาที
6. ลองเปิด steamlitweb `http://localhost:8501/` ถ้าใช้ได้จะมีหน้าตาแบบนี้ ![alt text](final\etc\fig\example1.png)
7. หยุดการใช้งานโดย Ctr+C ที่ cmd หรือ powershell หรือ `docker-compose down`

หมายเหตุ: MYSQL เปิด port ไว้ที่ localhost:3306
         MongoDB เปิด port ไว้ที่ localhost:27017
         Streamlit เปิด port ไว้ที่ localhost:8501