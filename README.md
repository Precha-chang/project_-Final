# Employee_hub
---
## Front end
- Bootstrap 5
- HTML 5
- CSS 3
## Deployment
- Vercel
## Database
- PosgestSQL (supabase)
## Back end
- Django Framework
## Template Bootstrap 5
 https://themewagon.com/themes/free-bootstrap-5-admin-dashboard-template-darkpan/

 ## link website Project
 https://project-final-drab.vercel.app

## สร้างฐานข้อมูล

- สร้าง ฐานข้อมูล ที่ไฟล์ models.py

```python
from django.db import models

# Create your models here.
class Department(models.Model):
  
    department = models.CharField(max_length=255)
  
    def __str__(self):
        return self.department
  
class Information(models.Model):

    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    gender = models.CharField(max_length=255,choices=(
        ("ชาย", "ชาย"),
        ("หญิง", "หญิง"),
    ))
    age = models.IntegerField()
    elevel = models.CharField(max_length=255,choices=(
        ("ปวช.", "ปวช."),
        ("ปวส.", "ปวส."),
        ("ปริญญาตรี", "ปริญญาตรี"),
        ("สูงกว่าปริญญาตรี", "สูงกว่าปริญญาตรี")
    ))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
  
  
    def __str__(self):
        return self.fname  
```

- register models ที่ admin.py

```python
from django.contrib import admin

# Register your models here.

from .models import Department, Information

@admin.register(Department)
class Admin(admin.ModelAdmin):
    list_display = ("department",)
    search_fields = ("department",)
  
@admin.register(Information)
class MajorAdmin(admin.ModelAdmin):
    list_display = (
        'fname', 
        'lname', 
        'gender',
        'age',
        'elevel',
        'department',
)
  
```

*การทำ admin register เพื่อที่เราจะสามารถเพิ่มข้อมูลเองได้*

## ภาพรวม webpage

 ![image](./img/img01.png)

 - แสดงประวัติพนักงานทั้งหมดได้
 - แสดงรายชื่อพนักงานแต่ละแผนกได้  =  จัดซื้อ  จัดหาลูกค้า    บริการหลังการขาย 
  - แสดงหน้าเกี่ยวกับบริษัท
   - แสดงผู้ดูแลระบบ





 By Dek Comsci 65

 @ Precha Chainara
