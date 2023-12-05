import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def draw_great_circle_route(output_path):
    fig = plt.figure(figsize=(20, 10))  # Adjusted figure size for a wider map
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Add natural earth features to the map
    ax.add_feature(cfeature.LAND, facecolor='lightgray')
    ax.add_feature(cfeature.OCEAN, facecolor='lightblue')
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS, linestyle=':')

    # New York and London coordinates
    new_york = (-74.0060, 40.7128)
    london = (-0.1278, 51.5074)

    # Draw the great circle route between New York and London
    ax.plot([new_york[0], london[0]], [new_york[1], london[1]],
            color='red', linestyle='--',
            transform=ccrs.Geodetic())

    # Show the entire globe
    ax.set_global()  # This method is used to display the full map

    # Optionally, you can remove the set_global line and adjust the figsize to show a full map
    # without setting an extent or global view.

    # Save the figure
    plt.savefig(output_path, bbox_inches='tight', dpi=300)
    plt.close()

# Call the function with the desired output file path
output_file_path = '/home/root1/projects/cs411/fa23-cs411-team080-HighLevel/output.png'
draw_great_circle_route(output_file_path)
