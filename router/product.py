
from fastapi import APIRouter, Form
from fastapi.responses import Response, HTMLResponse, PlainTextResponse



router = APIRouter(
    prefix='/product',
    tags = ['product']
    
    )

products = ["Phone","Laptop","Smart Watch","Phone Accessories"]

@router.post('/new')
def create_product(name: str = Form(...)):
    products.append(name)
    return products
@router.get('/all')
def get_all_product():
    #return products
    data = " ".join(products)
    return Response(content=data,media_type="text/plain")

@router.get('/{id}',responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Returns the HTML for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        },
        "description": "A cleartext error message"
    }
}
            )
def get_product(id:int):
    if id > len(products):
        out = "Product not available"
        return PlainTextResponse(content=out,media_type="text/plain")
    else:
        product = products[id]
        out = f"""
        <head>
            <styles>
            .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                background-color: lightblue;
                text-align: center;
            }}
            
            </styles>
        
        </head>
        <div class="product">{product}</div>

        """
        return HTMLResponse(content=out,media_type="text/html")

