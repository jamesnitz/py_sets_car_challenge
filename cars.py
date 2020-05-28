makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)
# # Here's HOWIE DO IT
# # 1 Declare a dictionary 
report_object = dict()
# loop over the makes  then declare another dictionary to hold the key:models and the value: a list of corresponding colors
for make in makes:
    make_model = dict()
    # the key is make 'toyota' and the value is another dictionary
    report_object[make[1]] = make_model
    # loop over the models then declare a list for the colors
    for model in models:
        color_options = list()
        # if a model (1, "prius", ***1***) == make (***1***, 'toyota)
        if model[2] == make[0]:
          # the make model dictionary gets a key of the model name 'prius' and a value of the list color_options
            make_model[model[1]] = color_options
            # loop over all the available car color options and if that model 'prius' is available in that color 'ivory'
            for color_option in available_car_colors:
                if color_option[0] == model[0]:
                  # then loop over all the colors and match them by their keys and append them to a models color list
                    for color in colors:
                        if color[0] == color_option[1]:
                            color_options.append(color[1])

# for key: 'toyota', value: { 'prius': ['charcoal', 'brick', 'ivory'], 'camry': ['black', 'red', 'white'] }
for (key, value) in report_object.items():
    print(f'{key}')
    print('---------------')
    for (model, colors) in value.items():
        a = f'{model} available in '
        for color in colors:
            a += f'{color}, '
        else: 
            a = a[slice(-2)] + f'.'
        print(a)
    print()

