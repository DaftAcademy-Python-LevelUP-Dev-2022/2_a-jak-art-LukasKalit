def greeter(function_to_decorate):
    def real_decorator(self):
        data = function_to_decorate(self).split(' ')
        data = [element.capitalize() for element in data]
        result = "Aloha"
        for i in data:
            result += f" {i}"
        return result
    return real_decorator



def sums_of_str_elements_are_equal(function_to_decorate):
    def real_decorator(self):
        sum_list = []
        data = function_to_decorate(self).split()
        
        for data_items in data:
            number = 0
            data_list = list(data_items)

            if data_list[0] == "-":
                for i in range(1, len(data_list)):
                    number += int(data_list[i])
                number *= -1
                    
            else:
                for i in range(len(data_list)):
                    number += int(data_list[i])

            sum_list.append(number)
        

        if sum_list[0] == sum_list[1]:
            result = f"{sum_list[0]} == {sum_list[1]}"
        else:
            result = f"{sum_list[0]} != {sum_list[1]}"

        return result

    return real_decorator


def format_output(*arguments):

    def real_decorator(function_to_decorate):
        def wrapper(*args, **kwargs):

            data = function_to_decorate(*args, **kwargs)
            print(data)
            result_dict = {}

            for i in arguments:
                key_word = i.split("__")


                if len(key_word) > 0:
                    string_chain = ""
                    for k in key_word:
                        Error_check = True

                        for j in data:
                            
                            if k == j:
                                Error_check = False

                                if data[j] == None or data[j] == '':
                                    string_chain += "Empty value"
                                else:
                                    string_chain += f"{data[j]} "
                        
                        if Error_check:
                            raise ValueError("ValueError")

                    string_chain=string_chain.strip()
                    result_dict[i] = string_chain
                
            return result_dict 
        return wrapper
    return real_decorator


def add_method_to_instance(class_object):
    def real_decorator(function_to_add):
        def wrapper():
            
            return function_to_add()

        setattr(class_object, function_to_add.__name__, staticmethod(function_to_add))
        return wrapper
    return real_decorator
