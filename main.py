userDB = "hidrotech123";
passwordDB = "admin123*";

print('Software tech hidroituango');
print('**************************');
userName = input('Digita tu usuario:');
userPassword = input('Digita tu contraseña:');

print("Exito iniciando sesión") if userDB == userName and passwordDB == userPassword else print("Fallaste");