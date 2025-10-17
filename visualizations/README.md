# Visualizations Directory

Store your charts, graphs, and plots here.

## File Formats

- **PNG**: Recommended for reports (good quality, smaller size)
- **SVG**: For scalable graphics
- **JPG**: For photos or complex images

## Naming Convention

Use descriptive names:
- `gdp_growth_2024.png`
- `inflation_trends_mexico.png`
- `unemployment_comparison.png`

## Creating Visualizations

### From Python
```python
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.plot(data['date'], data['value'])
plt.title('Title')
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.savefig('visualizations/chart_name.png', dpi=300, bbox_inches='tight')
plt.close()
```

### From R
```r
library(ggplot2)

ggplot(data, aes(x = date, y = value)) +
  geom_line() +
  labs(title = "Title", x = "X Label", y = "Y Label") +
  theme_minimal()

ggsave("visualizations/chart_name.png", width = 10, height = 6, dpi = 300)
```

## Current Visualizations

*No visualizations yet. Add your charts here!*
