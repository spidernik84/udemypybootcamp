
import one
print("top level in two.py")


one.func()

if __name__ == '__main__':
    print('two.py is being run directly!')
else:
    print('one.py has been imported!')