#include <stdio.h>
#include <dlfcn.h>

typedef void (*print_python_string_t)(const char *);

int main()
{
	void *handle = dlopen("./libPython.so", RTLD_LAZY);
	if (!handle)
	{
	fprintf(stderr, "Error opening library: %s\n", dlerror());
		return 1;
	}

	print_python_string_t print_python_string =
		(print_python_string_t)dlsym(handle, "print_python_string");
	if (!print_python_string)
	{
		fprintf(stderr, "Error finding symbol: %s\n", dlerror());
		dlclose(handle);
		return 1;
	}

	const char *s;

	s = "The spoon does not exist";
	print_python_string(s);

	s = "ложка не существует";
	print_python_string(s);

	s = "La cuillère n'existe pas";
	print_python_string(s);

	s = "勺子不存在";
	print_python_string(s);

	s = "숟가락은 존재하지 않는다.";
	print_python_string(s);

	s = "スプーンは存在しない";
	print_python_string(s);

	s = "The spoon does not exist";
	print_python_string(s);
	dlclose(handle);
	return 0;
}
