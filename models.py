# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccessPermission(models.Model):
    role_id = models.IntegerField()
    allow_page = models.CharField(max_length=255)
    added_on = models.DateTimeField()
    added_by = models.CharField(max_length=25)
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'access_permission'


class Admin(models.Model):
    admin_id = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    adm_img = models.CharField(max_length=100)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=80)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=80)
    expiry = models.DateField(blank=True, null=True)
    added_on = models.DateTimeField()
    updated_on = models.DateField(blank=True, null=True)
    reg_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'admin'


class Appointments(models.Model):
    appointment_id = models.CharField(unique=True, max_length=16)
    patient_id = models.CharField(max_length=14)
    appointment_date = models.CharField(max_length=12)
    patient_name = models.CharField(max_length=30)
    patient_gurdian_name = models.CharField(max_length=30)
    patient_email = models.CharField(max_length=30)
    patient_phno = models.CharField(max_length=10)
    patient_age = models.IntegerField()
    patient_weight = models.IntegerField()
    patient_gender = models.CharField(max_length=8)
    patient_addres1 = models.CharField(max_length=255)
    patient_addres2 = models.CharField(max_length=255)
    patient_ps = models.CharField(max_length=50)
    patient_dist = models.CharField(max_length=50)
    patient_pin = models.CharField(max_length=7)
    patient_state = models.CharField(max_length=50)
    doctor_id = models.CharField(max_length=6, blank=True, null=True)
    patient_doc_shift = models.CharField(max_length=255)
    added_by = models.CharField(max_length=20)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=20)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'appointments'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ClinicInfo(models.Model):
    hospital_id = models.CharField(primary_key=True, max_length=30)
    logo = models.CharField(max_length=100)
    hospital_name = models.CharField(max_length=150)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    dist = models.CharField(max_length=50)
    pin = models.CharField(max_length=7)
    health_care_state = models.CharField(max_length=50)
    hospital_email = models.CharField(max_length=50)
    hospital_phno = models.CharField(max_length=10)
    appointment_help_line = models.CharField(max_length=10)
    main_desc = models.CharField(max_length=400)
    footer_desc = models.CharField(max_length=150)
    book_appointment_text = models.CharField(max_length=255)
    subscribe_text = models.CharField(max_length=70)
    admin_id = models.CharField(max_length=20)
    added_on = models.DateField()

    class Meta:
        managed = False
        db_table = 'clinic_info'


class ContactDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=355)

    class Meta:
        managed = False
        db_table = 'contact_details'


class CurrentStock(models.Model):
    stock_in_details_id = models.IntegerField()
    product_id = models.CharField(max_length=20)
    batch_no = models.CharField(max_length=20)
    exp_date = models.CharField(max_length=7)
    distributor_id = models.IntegerField()
    weightage = models.IntegerField()
    unit = models.CharField(max_length=24)
    qty = models.IntegerField()
    loosely_count = models.IntegerField()
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    loosely_price = models.DecimalField(max_digits=8, decimal_places=2)
    ptr = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.IntegerField()
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'current_stock'


class Distributor(models.Model):
    name = models.CharField(max_length=155)
    gst_id = models.CharField(max_length=16)
    address = models.CharField(max_length=255)
    area_pin_code = models.BigIntegerField()
    phno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    dsc = models.CharField(max_length=355)
    status = models.IntegerField()
    new = models.IntegerField()
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'distributor'


class DistributorRequest(models.Model):
    dist_id = models.IntegerField()
    name = models.CharField(max_length=155)
    address = models.CharField(max_length=255)
    area_pin_code = models.BigIntegerField()
    gst_id = models.CharField(max_length=20)
    phno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    dsc = models.CharField(max_length=355)
    req_dsc = models.CharField(max_length=355)
    added_by = models.CharField(max_length=20)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=20)
    updated_on = models.DateTimeField()
    status = models.IntegerField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'distributor_request'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DoctorCategory(models.Model):
    doctor_category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_descreption = models.CharField(max_length=500)
    doctor_id = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'doctor_category'


class DoctorTiming(models.Model):
    doc_timing_id = models.IntegerField(primary_key=True)
    doctor_id = models.IntegerField()
    days = models.CharField(max_length=25)
    shift = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'doctor_timing'


class Doctors(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    doctor_reg_no = models.CharField(max_length=12)
    doctor_name = models.CharField(max_length=50)
    doctor_specialization = models.ForeignKey(DoctorCategory, models.DO_NOTHING, db_column='doctor_specialization')
    doctor_degree = models.CharField(max_length=50)
    also_with = models.CharField(max_length=100)
    doctor_address = models.CharField(max_length=255)
    doctor_email = models.CharField(max_length=30)
    doctor_phno = models.CharField(max_length=10)
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'doctors'


class EmpRole(models.Model):
    desig_name = models.CharField(max_length=30)
    add_by = models.CharField(max_length=30)
    add_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'emp_role'


class Employees(models.Model):
    emp_id = models.AutoField(primary_key=True)
    admin_id = models.CharField(max_length=20)
    emp_username = models.CharField(max_length=15)
    emp_name = models.CharField(max_length=30)
    emp_img = models.CharField(max_length=100)
    emp_role = models.IntegerField()
    emp_email = models.CharField(max_length=100)
    contact = models.BigIntegerField(blank=True, null=True)
    emp_address = models.CharField(max_length=255)
    emp_password = models.CharField(max_length=255)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employees'


class Gst(models.Model):
    percentage = models.CharField(max_length=2)
    added_by = models.CharField(max_length=12)
    added_on = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'gst'


class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    customer_id = models.CharField(max_length=20)
    total_amount = models.IntegerField()
    date = models.DateTimeField()
    added_by = models.CharField(max_length=155)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'invoice'


class ItemUnit(models.Model):
    name = models.CharField(max_length=30)
    added_on = models.DateTimeField()
    added_by = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'item_unit'


class LabAppointments(models.Model):
    id = models.BigAutoField(primary_key=True)
    bill_id = models.CharField(max_length=30)
    patient_id = models.CharField(max_length=14)
    prefered_doctor_id = models.CharField(max_length=80)
    test_ids = models.CharField(max_length=255)
    prices = models.CharField(max_length=355)
    discount = models.CharField(max_length=355)
    after_discount = models.CharField(max_length=355)
    total_amount = models.CharField(max_length=10)
    cgst = models.CharField(max_length=12)
    sgst = models.CharField(max_length=12)
    paid_amount = models.CharField(max_length=12)
    test_date = models.DateTimeField()
    added_by = models.CharField(max_length=20)
    added_on = models.DateTimeField()
    update_by = models.IntegerField()
    update_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'lab_appointments'


class LabBilling(models.Model):
    bill_id = models.BigIntegerField(primary_key=True)
    bill_date = models.CharField(max_length=24)
    patient_id = models.CharField(max_length=14)
    refered_doctor = models.CharField(max_length=55)
    test_date = models.DateField()
    total_amount = models.CharField(max_length=8)
    discount = models.CharField(max_length=6)
    total_after_discount = models.CharField(max_length=8)
    cgst = models.CharField(max_length=3)
    sgst = models.CharField(max_length=3)
    paid_amount = models.CharField(max_length=8)
    due_amount = models.CharField(max_length=8)
    status = models.CharField(max_length=12)
    added_by = models.CharField(max_length=20)
    added_on = models.DateTimeField()
    update_by = models.CharField(max_length=20)
    update_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'lab_billing'


class LabBillingDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    bill_id = models.BigIntegerField()
    billing_date = models.CharField(max_length=24)
    test_date = models.DateField()
    test_id = models.CharField(max_length=12)
    test_price = models.CharField(max_length=8)
    percentage_of_discount_on_test = models.CharField(max_length=6)
    price_after_discount = models.CharField(max_length=8)
    added_by = models.CharField(max_length=20)
    added_on = models.DateTimeField()
    update_by = models.CharField(max_length=20)
    update_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lab_billing_details'


class LabReport(models.Model):
    bill_id = models.IntegerField()
    patient_id = models.CharField(max_length=30)
    admin_id = models.CharField(max_length=20)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lab_report'


class LabReportDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    report_id = models.IntegerField()
    test_id = models.CharField(max_length=30)
    test_value = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'lab_report_detail'


class LandingPlans(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'landing_plans'


class LoginActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.CharField(max_length=20)
    emp_id = models.IntegerField()
    login_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'login_activity'


class LooseUnit(models.Model):
    unit_id = models.IntegerField()
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    added_by = models.CharField(max_length=25)
    added_on = models.DateTimeField()
    updated_by = models.DateTimeField()
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'loose_unit'


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=30)
    dsc = models.CharField(max_length=400)
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    status = models.IntegerField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'manufacturer'


class ManufacturerRequest(models.Model):
    manu_id = models.IntegerField()
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=30)
    dsc = models.CharField(max_length=400)
    req_dsc = models.CharField(max_length=400)
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    status = models.IntegerField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'manufacturer_request'


class PackagingType(models.Model):
    unit_name = models.CharField(max_length=20)
    added_by = models.CharField(max_length=25)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    status = models.IntegerField()
    new = models.IntegerField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'packaging_type'


class PacktypeRequest(models.Model):
    pack_id = models.IntegerField()
    unit_name = models.CharField(max_length=20)
    req_dsc = models.CharField(max_length=400)
    added_by = models.CharField(max_length=25)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    status = models.IntegerField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'packtype_request'


class PatientDetails(models.Model):
    patient_id = models.CharField(max_length=20)
    name = models.CharField(max_length=80)
    gurdian_name = models.CharField(max_length=80)
    email = models.CharField(max_length=30)
    phno = models.CharField(max_length=10)
    age = models.CharField(max_length=12)
    gender = models.CharField(max_length=8)
    address_1 = models.CharField(max_length=255)
    address_2 = models.CharField(max_length=255)
    patient_ps = models.CharField(max_length=50)
    patient_dist = models.CharField(max_length=50)
    patient_pin = models.CharField(max_length=7)
    patient_state = models.CharField(max_length=50)
    visited = models.CharField(max_length=10)
    lab_visited = models.CharField(max_length=10)
    added_on = models.DateTimeField()
    added_by = models.CharField(max_length=30)
    update_on = models.DateTimeField()
    update_by = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'patient_details'


class PharmacyInvoice(models.Model):
    invoice_id = models.BigIntegerField()
    item_id = models.IntegerField()
    item_name = models.CharField(max_length=28)
    batch_no = models.CharField(max_length=16)
    weatage = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=7)
    qty = models.IntegerField()
    loosely_count = models.IntegerField()
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    disc = models.CharField(max_length=5)
    taxable = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    added_by = models.CharField(max_length=16)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pharmacy_invoice'


class ProductImages(models.Model):
    product_id = models.CharField(max_length=24)
    image = models.CharField(max_length=666)
    set_priority = models.CharField(max_length=20)
    added_by = models.CharField(max_length=16)
    status = models.IntegerField()
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'product_images'


class ProductRequest(models.Model):
    product_id = models.CharField(max_length=30)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55, db_comment='Like: allopathy, drug, otc, etc.')
    packaging_type = models.IntegerField(db_comment='Like: stript, bottole, tube etc.')
    unit_quantity = models.CharField(max_length=12, db_comment='Number of qantity')
    unit = models.CharField(max_length=30, db_comment='Like: tablets, syrup etc.')
    power = models.CharField(max_length=6, db_comment='Like: 10, 15, 20, 200 etc.')
    mrp = models.DecimalField(max_digits=12, decimal_places=2)
    gst = models.IntegerField()
    hsno_number = models.CharField(max_length=21)
    old_prod_id = models.CharField(max_length=25)
    comp1 = models.CharField(max_length=255)
    comp2 = models.CharField(max_length=255)
    req_dsc = models.CharField(max_length=555)
    prod_req_status = models.IntegerField()
    old_prod_flag = models.IntegerField()
    requested_on = models.DateTimeField()
    requested_by = models.CharField(max_length=20)
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'product_request'


class ProductType(models.Model):
    name = models.CharField(max_length=55)
    status = models.IntegerField()
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'product_type'


class Products(models.Model):
    product_id = models.CharField(primary_key=True, max_length=20)
    manufacturer = models.ForeignKey(Manufacturer, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=55)
    power = models.CharField(max_length=6)
    dsc = models.CharField(max_length=255)
    unit_quantity = models.CharField(max_length=12, db_comment='number of quantity')
    unit = models.ForeignKey('QuantityUnit', models.DO_NOTHING, db_comment='Like: Pieces, ml, gm etc')
    unit_0 = models.ForeignKey(ItemUnit, models.DO_NOTHING, db_column='unit', db_comment='Like: Tablets, Capsule etc')  # Field renamed because of name conflict.
    packaging_type = models.ForeignKey(PackagingType, models.DO_NOTHING, db_column='packaging_type', db_comment='Like: Strip, Bottle etc')
    mrp = models.CharField(max_length=12)
    gst = models.CharField(max_length=6, blank=True, null=True)
    comp_1 = models.CharField(max_length=500, blank=True, null=True)
    comp_2 = models.CharField(max_length=500, blank=True, null=True)
    hsno_number = models.IntegerField()
    edit_request_flag = models.SmallIntegerField()
    verified = models.IntegerField()
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'products'


class QuantityUnit(models.Model):
    short_name = models.CharField(max_length=10)
    full_name = models.CharField(max_length=30)
    status = models.IntegerField()
    new = models.IntegerField()
    added_by = models.CharField(max_length=25)
    added_on = models.DateTimeField()
    updated_by = models.DateTimeField()
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'quantity_unit'


class Registration(models.Model):
    id = models.IntegerField()
    mobile_number = models.CharField(max_length=10)
    otp = models.CharField(max_length=6)
    time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'registration'


class RolePermision(models.Model):
    role_id = models.IntegerField()
    allow = models.CharField(max_length=55)
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'role_permision'


class SalesReturn(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_id = models.BigIntegerField()
    patient_id = models.CharField(max_length=18)
    bill_date = models.DateField()
    return_date = models.DateField()
    items = models.IntegerField()
    total_qty = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    refund_amount = models.DecimalField(max_digits=10, decimal_places=2)
    refund_mode = models.CharField(max_length=12)
    status = models.CharField(max_length=14)
    added_by = models.CharField(max_length=14)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'sales_return'


class SalesReturnDetails(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoice_id = models.BigIntegerField()
    sales_return_id = models.BigIntegerField()
    item_id = models.IntegerField()
    product_id = models.CharField(max_length=20)
    batch_no = models.CharField(max_length=14)
    weatage = models.CharField(max_length=14)
    exp = models.CharField(max_length=7)
    mrp = models.FloatField()
    ptr = models.DecimalField(max_digits=8, decimal_places=2)
    disc = models.IntegerField()
    gst = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    taxable = models.DecimalField(max_digits=8, decimal_places=2)
    return_qty = models.IntegerField()
    refund_amount = models.DecimalField(max_digits=8, decimal_places=2)
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'sales_return_details'


class StockIn(models.Model):
    id = models.BigAutoField(primary_key=True)
    distributor_id = models.IntegerField()
    distributor_bill = models.CharField(max_length=20)
    items = models.IntegerField()
    total_qty = models.CharField(max_length=12)
    bill_date = models.CharField(max_length=10)
    due_date = models.CharField(max_length=10)
    payment_mode = models.CharField(max_length=24)
    gst = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    added_by = models.CharField(max_length=15)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stock_in'


class StockInDetails(models.Model):
    stokin_id = models.BigIntegerField(db_column='stokIn_id')  # Field name made lowercase.
    product_id = models.CharField(max_length=20)
    distributor_bill = models.CharField(max_length=20)
    batch_no = models.CharField(max_length=20)
    mfd_date = models.CharField(max_length=10)
    exp_date = models.CharField(max_length=10)
    weightage = models.IntegerField()
    unit = models.CharField(max_length=24)
    qty = models.IntegerField()
    free_qty = models.IntegerField()
    loosely_count = models.IntegerField()
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    ptr = models.DecimalField(max_digits=8, decimal_places=2, db_comment='Price to retailer on QTY ')
    discount = models.IntegerField(db_comment='Percentage of discount on PTR')
    d_price = models.DecimalField(max_digits=6, decimal_places=2, db_comment='after discount on PTR of Purchased Quantity')
    base = models.DecimalField(max_digits=8, decimal_places=2, db_comment='Average Price of a single (including free qty) item by discounted price (qty * d_price / qty+free_qty)')
    gst = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    update_emp_id = models.CharField(max_length=24)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_in_details'


class StockOut(models.Model):
    invoice_id = models.BigIntegerField(primary_key=True)
    customer_id = models.CharField(max_length=20)
    reff_by = models.CharField(max_length=55)
    items = models.IntegerField()
    qty = models.IntegerField()
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    disc = models.CharField(max_length=5)
    gst = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_mode = models.CharField(max_length=25)
    status = models.CharField(max_length=16)
    bill_date = models.CharField(max_length=10)
    added_by = models.CharField(max_length=16)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stock_out'


class StockOutDetails(models.Model):
    invoice_id = models.BigIntegerField()
    item_id = models.IntegerField()
    product_id = models.CharField(max_length=20)
    item_name = models.CharField(max_length=50)
    batch_no = models.CharField(max_length=12)
    exp_date = models.CharField(max_length=10)
    weightage = models.CharField(max_length=6)
    unit = models.CharField(max_length=24)
    qty = models.CharField(max_length=10)
    loosely_count = models.CharField(max_length=10)
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    ptr = models.DecimalField(max_digits=8, decimal_places=2)
    discount = models.CharField(max_length=3)
    gst = models.CharField(max_length=3)
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    margin = models.DecimalField(max_digits=8, decimal_places=2)
    taxable = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=11, decimal_places=2)
    updated_by = models.CharField(max_length=24)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_out_details'


class StockReturn(models.Model):
    id = models.BigIntegerField(primary_key=True)
    stockin_id = models.BigIntegerField()
    distributor_id = models.IntegerField()
    bill_no = models.CharField(max_length=20)
    return_date = models.DateField()
    items = models.IntegerField()
    total_qty = models.IntegerField()
    gst_amount = models.DecimalField(max_digits=8, decimal_places=2)
    refund_mode = models.CharField(max_length=14)
    refund_amount = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10)
    added_by = models.CharField(max_length=14)
    added_on = models.DateTimeField()
    updated_by = models.CharField(max_length=15)
    updated_on = models.DateTimeField()
    admin_id = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'stock_return'


class StockReturnDetails(models.Model):
    stock_return_id = models.BigIntegerField()
    stokin_details_id = models.IntegerField(db_column='stokIn_details_id')  # Field name made lowercase.
    product_id = models.CharField(max_length=14)
    dist_bill_no = models.CharField(max_length=30)
    batch_no = models.CharField(max_length=18)
    exp_date = models.CharField(max_length=7)
    unit = models.CharField(max_length=24)
    purchase_qty = models.IntegerField()
    free_qty = models.IntegerField()
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    ptr = models.DecimalField(max_digits=8, decimal_places=2)
    gst = models.IntegerField()
    disc = models.IntegerField()
    return_qty = models.IntegerField()
    return_free_qty = models.IntegerField()
    refund_amount = models.DecimalField(max_digits=8, decimal_places=2)
    updated_by = models.CharField(max_length=20)
    updated_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'stock_return_details'


class SubTests(models.Model):
    sub_test_name = models.CharField(max_length=300)
    unit = models.CharField(max_length=10)
    parent_test_id = models.CharField(max_length=6)
    age_group = models.CharField(max_length=15)
    test_preparation = models.CharField(max_length=500)
    test_dsc = models.CharField(max_length=300)
    price = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'sub_tests'


class Subscription(models.Model):
    id = models.BigAutoField(primary_key=True)
    admin_id = models.CharField(max_length=20)
    plan = models.IntegerField()
    start = models.DateField()
    end = models.DateField()
    paid = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'subscription'


class SuperAdmin(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    adm_img = models.CharField(max_length=100)
    username = models.CharField(max_length=24)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=80)
    mobile_no = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    added_on = models.DateTimeField()
    updated_on = models.DateField()
    expiry = models.DateField()

    class Meta:
        managed = False
        db_table = 'super_admin'


class TestsTypes(models.Model):
    image = models.CharField(max_length=155)
    test_type_name = models.CharField(max_length=100)
    provided_by = models.TextField()
    dsc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tests_types'
