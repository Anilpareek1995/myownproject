from django.shortcuts import render
import pandas as pd
def home(request):
    df =pd.read_csv("crimedata.csv")
    df.rename(columns={"STATE/UT":"STATE"}, inplace=True)
    rs = df.groupby("STATE")["Total Female"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)

    table_content = df.to_html(index=None)
    table_content = table_content.replace("", "")
    table_content = table_content.replace('class="dataframe"', "class='table table-striped'")
    table_content = table_content.replace('border="1"', "")

    context = {"categories": categories, 'values': values, 'table_data': table_content}
    return render(request, 'layout.html', context=context)
