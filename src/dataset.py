import time

read_time = 0.5
color_options = {"magenta", "purple", "orange", "blue"}
emitter_options = {"nychta", "avgi", "mygeeto", "enforcer"}
sleeve_options = {"nychta", "avgi", "mygeeto", "enforcer"}
material_options = {"aurodium", "osmiridium", "durite", "matte"}
customization_options = {
    "color": color_options,
    "emitter": emitter_options,
    "sleeve": sleeve_options,
    "material": material_options,
}
customized_data = {"color": None, "emitter": None, "sleeve": None, "material": None}


def display_options(options):
    i = 0
    string = ""
    for opt in options:
        if string == "":
            string = string + opt
        elif i < len(options) - 1:
            string = string + ", " + opt
        else:
            string = string + ", or " + opt
        i += 1
    return string


def select_option(prompt, options):
    while True:
        response = input(prompt).lower()
        for opt in options:
            if response == opt:
                return response
        print("Invalid entry! Please try again.")


def display_specs():
    print("-------------------------------")
    print("color: ", customized_data["color"])
    print("emitter: ", customized_data["emitter"])
    print("sleeve: ", customized_data["sleeve"])
    print("material: ", customized_data["material"])
    print("-------------------------------")


print("Welcome to the lightsaber customization menu!")
print("Here you will customize your very own lightsaber. Hope you're ready...")
while True:
    time.sleep(read_time)
    display_customization_options = display_options(customization_options)
    component_selection_prompt = (
        "What do you want to customize... " + display_customization_options + "?: "
    )
    component_selection = select_option(
        component_selection_prompt, customization_options
    )
    component_options = customization_options[component_selection]
    display_component_options = display_options(component_options)
    component_type_prompt = (
        "What type of "
        + component_selection
        + " do you want... "
        + display_component_options
        + "?: "
    )
    component_type_selection = select_option(component_type_prompt, component_options)
    time.sleep(read_time)
    customized_data[component_selection] = component_type_selection
    print("Here is what your lightsaber currently looks like... ")
    time.sleep(read_time)
    display_specs()
    time.sleep(read_time)
    wish_to_continue = input(
        "Do you wish to keep editing your lightsaber? Type 'y' or 'yes' to continue, or you will be exited out of the menu: "
    )
    if wish_to_continue.lower() != "y" and wish_to_continue.lower() != "yes":
        break
time.sleep(read_time)
print("Here are your finalized specs... ")
time.sleep(read_time)
display_specs()
time.sleep(read_time)
print("We hope you had a great experience with the lightsaber customization menu!")
