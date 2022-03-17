<class 'pandas.core.frame.DataFrame'>
RangeIndex: 2919 entries, 0 to 2918
Data columns (total 81 columns):
 #   Column         Non-Null Count  Dtype       Tier3 Tier2 Tier1 
---  ------         --------------  -----       ----- ----- -----
 0   Id             2919 non-null   int64       Unuse
 1   MSSubClass     2919 non-null   int64       Use   Use
 2   MSZoning       2915 non-null   object      Use   Use
 3   LotFrontage    2433 non-null   float64     Unuse
 4   LotArea        2919 non-null   int64       Use   Use
 5   Street         2919 non-null   object      Unuse
 6   Alley          198 non-null    object      Unuse
 7   LotShape       2919 non-null   object      Unuse
 8   LandContour    2919 non-null   object      Use   Use
 9   Utilities      2917 non-null   object      Unuse  
 10  LotConfig      2919 non-null   object      Use   Unuse
 11  LandSlope      2919 non-null   object      Unuse
 12  Neighborhood   2919 non-null   object      Use   Use
 13  Condition1     2919 non-null   object      Use   Use
 14  Condition2     2919 non-null   object      Use   Use
 15  BldgType       2919 non-null   object      Use   Unuse
 16  HouseStyle     2919 non-null   object      Use   Use
 17  OverallQual    2919 non-null   int64       Use   Use
 18  OverallCond    2919 non-null   int64       Unuse
 ---Choose Latest One
 19  YearBuilt      2919 non-null   int64       Use   Use
 20  YearRemodAdd   2919 non-null   int64       Use   Use
 ---RN
 21  RoofStyle      2919 non-null   object      Unuse
 22  RoofMatl       2919 non-null   object      Unuse
 ---外壁のタイプ
 23  Exterior1st    2918 non-null   object      Use   Use
 24  Exterior2nd    2918 non-null   object      Unuse
 25  MasVnrType     2895 non-null   object      Unuse
 26  MasVnrArea     2896 non-null   float64     Unuse
 27  ExterQual      2919 non-null   object      Unuse
 28  ExterCond      2919 non-null   object      Unuse
 29  Foundation     2919 non-null   object      Use   Unuse
 #Base
 30  BsmtQual       2838 non-null   object      Unuse
 31  BsmtCond       2837 non-null   object      Unuse
 32  BsmtExposure   2837 non-null   object      Unuse
 33  BsmtFinType1   2840 non-null   object      Unuse
 34  BsmtFinSF1     2918 non-null   float64     Unuse
 35  BsmtFinType2   2839 non-null   object      Unuse
 36  BsmtFinSF2     2918 non-null   float64     Unuse
 37  BsmtUnfSF      2918 non-null   float64     Unuse
 38  TotalBsmtSF    2918 non-null   float64     Use   Use
 39  Heating        2919 non-null   object      Unuse
 40  HeatingQC      2919 non-null   object      Unuse
 41  CentralAir     2919 non-null   object      Unuse
 42  Electrical     2918 non-null   object      Unuse
 43  1stFlrSF       2919 non-null   int64       Use   Use
 44  2ndFlrSF       2919 non-null   int64       Use   Use
 45  LowQualFinSF   2919 non-null   int64       Unuse
 46  GrLivArea      2919 non-null   int64       Use   Use
 47  BsmtFullBath   2917 non-null   float64     Unuse
 48  BsmtHalfBath   2917 non-null   float64     Unuse
 49  FullBath       2919 non-null   int64       Unuse
 50  HalfBath       2919 non-null   int64       Unuse
 51  BedroomAbvGr   2919 non-null   int64       Unuse
 52  KitchenAbvGr   2919 non-null   int64       Unuse
 53  KitchenQual    2918 non-null   object      Unuse
 54  TotRmsAbvGrd   2919 non-null   int64       Use   Use
 55  Functional     2917 non-null   object      Unuse
 56  Fireplaces     2919 non-null   int64       Unuse
 57  FireplaceQu    1499 non-null   object      Unuse
 58  GarageType     2762 non-null   object      Unuse
 59  GarageYrBlt    2760 non-null   float64     Unuse
 60  GarageFinish   2760 non-null   object      Unuse
 61  GarageCars     2918 non-null   float64     Unuse
 62  GarageArea     2918 non-null   float64     Use   Unuse
 63  GarageQual     2760 non-null   object      Unuse
 64  GarageCond     2760 non-null   object      Unuse
 65  PavedDrive     2919 non-null   object      Unuse
 66  WoodDeckSF     2919 non-null   int64       Use   Unuse
 67  OpenPorchSF    2919 non-null   int64       Use   Unuse
 68  EnclosedPorch  2919 non-null   int64       Unuse
 69  3SsnPorch      2919 non-null   int64       Unuse
 70  ScreenPorch    2919 non-null   int64       Unuse
 71  PoolArea       2919 non-null   int64       Unuse
 72  PoolQC         10 non-null     object      Unuse
 73  Fence          571 non-null    object      Unuse
 74  MiscFeature    105 non-null    object      Unuse
 75  MiscVal        2919 non-null   int64       Unuse
 76  MoSold         2919 non-null   int64       Unuse
 77  YrSold         2919 non-null   int64       Unuse
 78  SaleType       2918 non-null   object      Use   Use
 79  SaleCondition  2919 non-null   object      Use   Use
 80  SalePrice      1460 non-null   float64     -----
dtypes: float64(12), int64(26), object(43)
memory usage: 1.8+ MB