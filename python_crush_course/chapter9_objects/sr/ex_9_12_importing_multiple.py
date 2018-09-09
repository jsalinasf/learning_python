from admin import Admin

admin01 = Admin("Jorge", "Salinas", "Quito", "Male")
admin02 = Admin("Rodrigo", "Figueroa", "Buenos Aires", "Male")

print("\nAdding Privileges for: {} {}".format(admin01.first, admin01.last))
admin01.admin_add_privileges()
admin01.admin_show_privileges()

print("\nAdding Privileges for: {} {}".format(admin02.first, admin02.last))
admin02.admin_add_privileges()
admin02.admin_show_privileges()