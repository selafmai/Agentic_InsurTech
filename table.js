Table Creation

| Column Name | Data Type | Description | Key Characteristics | Example Use Case |
|------------|-----------|-------------|---------------------|-----------------|
| `id` | UUID | Unique global identifier | - Automatically generated<br>- Ensures record uniqueness<br>- Random, non-sequential | Tracking specific insurance transaction globally |
| `prompt` | TEXT | Initial context description | - Human-readable summary<br>- Captures scenario essence<br>- Input trigger for AI analysis | "Damaged roof after storm - vehicle parked nearby" |
| `intent` | JSON/JSONB | Rich, structured metadata | - Flexible schema<br>- Nested AI insights<br>- Multi-dimensional information | Storing image caption, object detection, sentiment |
| `underwriting_score` | NUMERIC(5,2) | AI-generated risk assessment | - Ranges 0.00-999.99<br>- Precise risk quantification<br>- Decimal precision | 87.5 (high-risk scenario) |
| `risk_category` | VARCHAR(50) | Risk level classification | - Predefined categories<br>- Quick filtering<br>- Standardized risk mapping | "High Risk", "Moderate Risk" |
| `coverage_type` | VARCHAR(100) | Specific insurance protection | - Detailed coverage description<br>- Precise policy definition<br>- Granular insurance type | "Comprehensive Property Damage" |
| `insurance_type` | VARCHAR(100) | Broad insurance category | - High-level classification<br>- Reporting and analysis<br>- Market segmentation | "Residential Storm Insurance" |
| `policy_number` | VARCHAR(50) | Unique policy identifier | - Structured format<br>- Easy tracking<br>- Systematic numbering | "STORM-2024-0001" |
| `price` | NUMERIC(10,2) | Insurance policy cost | - Precise pricing<br>- Supports large values<br>- Decimal precision | $1,250.00 for storm damage |
| `prevention_plan` | TEXT | Risk mitigation strategy | - Detailed action items<br>- Proactive risk management<br>- Contextual recommendations | "Immediate roof tarping, vehicle repair" |
| `created_at` | TIMESTAMP WITH TIME ZONE | Record creation timestamp | - Automatic logging<br>- Timezone aware<br>- Audit trail | 2024-04-12 15:30:45+00 |



The CREATE TABLE statement defines the structure of the insurance_transactions table. It includes various columns:

id: A unique identifier for each transaction, automatically generated.
prompt: The initial request or description of the insured item or situation.
intent: A JSON object containing extracted information, such as image captions, object detection results, and sentiment analysis. This represents the AI's understanding of the prompt.
underwriting_score: A numerical score representing the assessed risk.
risk_category: A categorical representation of the risk level (e.g., High, Moderate, Low).
coverage_type: The type of insurance coverage provided.
insurance_type: The specific category of insurance.
policy_number: The assigned policy number.
price: The price of the insurance policy.
prevention_plan: Recommended preventative measures or actions.
created_at: A timestamp recording when the transaction was created.


-- Create the InsurTech CRM Transactional Table
CREATE TABLE insurance_transactions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    prompt TEXT NOT NULL,
    intent JSON NOT NULL,
    underwriting_score NUMERIC(5,2),
    risk_category VARCHAR(50),
    coverage_type VARCHAR(100),
    insurance_type VARCHAR(100),
    policy_number VARCHAR(50),
    price NUMERIC(10,2),
    prevention_plan TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert Sample Data Demonstrating AI-Enhanced Underwriting Workflow
INSERT INTO insurance_transactions (
    prompt, 
    intent, 
    underwriting_score, 
    risk_category, 
    coverage_type, 
    insurance_type, 
    policy_number, 
    price, 
    prevention_plan
) VALUES 
(
    'Damaged roof after storm - vehicle parked nearby with visible dents',
    '{
        "image_caption": "Residential roof with storm damage, adjacent car showing hail impact",
        "object_detection": {
            "roof_damage_severity": "high",
            "hail_impact_area": "extensive",
            "vehicle_condition": "moderate damage"
        },
        "sentiment": "urgent repair needed"
    }::jsonb,
    87.5,
    'High Risk',
    'Comprehensive Property and Vehicle Damage',
    'Residential Storm Insurance',
    'STORM-2024-0001',
    1250.00,
    'Immediate roof tarping, vehicle dent repair assessment, emergency mitigation plan'
),
(
    'Classic car with vintage restoration - potential collector''s item',
    '{
        "image_caption": "Meticulously restored 1967 Ford Mustang in pristine condition",
        "object_detection": {
            "car_age": "vintage",
            "restoration_quality": "exceptional",
            "preservation_state": "mint"
        },
        "sentiment": "high-value collectible"
    }::jsonb,
    92.3,
    'Low Risk',
    'Specialized Collector Vehicle Insurance',
    'Classic Car Insurance',
    'CLASSIC-2024-0002',
    3500.00,
    'Agreed value protection, specialized restoration coverage, museum-grade preservation plan'
),
(
    'Commercial drone fleet for agricultural monitoring',
    '{
        "image_caption": "Multiple agricultural drones surveying large farmland",
        "object_detection": {
            "drone_count": 5,
            "operational_area": "large agricultural field",
            "technology_sophistication": "advanced"
        },
        "sentiment": "professional equipment"
    }::jsonb,
    85.7,
    'Moderate Risk',
    'Commercial Equipment and Liability',
    'Agricultural Technology Insurance',
    'DRONE-2024-0003',
    2750.50,
    'Comprehensive drone fleet coverage, equipment replacement, liability protection'
),
(
    'Renewable energy solar farm installation',
    '{
        "image_caption": "Large-scale solar panel installation on open terrain",
        "object_detection": {
            "panel_count": "extensive",
            "installation_complexity": "high",
            "terrain_suitability": "optimal"
        },
        "sentiment": "sustainable infrastructure"
    }::jsonb,
    90.1,
    'Low Risk',
    'Renewable Energy Infrastructure Insurance',
    'Green Technology Insurance',
    'SOLAR-2024-0004',
    5000.75,
    'Performance guarantee, equipment breakdown, environmental impact coverage'
),
(
    'High-rise building construction site with multiple cranes',
    '{
        "image_caption": "Urban construction site with multiple cranes and scaffolding",
        "object_detection": {
            "crane_count": 3,
            "construction_stage": "mid-development",
            "site_complexity": "high"
        },
        "sentiment": "complex construction project"
    }::jsonb,
    88.9,
    'High Risk',
    'Construction All-Risk Insurance',
    'Commercial Construction Insurance',
    'BUILD-2024-0005',
    7500.25,
    'Comprehensive site coverage, worker protection, equipment and material insurance'
),
(
    'Advanced medical research laboratory equipment',
    '{
        "image_caption": "State-of-the-art medical research facility with sophisticated equipment",
        "object_detection": {
            "equipment_value": "high",
            "research_complexity": "advanced",
            "technological_sophistication": "cutting-edge"
        },
        "sentiment": "critical research infrastructure"
    }::jsonb,
    93.6,
    'Specialized Risk',
    'Scientific Equipment and Research Liability',
    'Research Facility Insurance',
    'RESEARCH-2024-0006',
    12000.00,
    'Full equipment replacement, research interruption coverage, liability protection'
),
(
    'Autonomous delivery robot fleet for urban logistics',
    '{
        "image_caption": "Multiple autonomous delivery robots navigating city streets",
        "object_detection": {
            "robot_count": 10,
            "operational_environment": "urban",
            "technological_innovation": "high"
        },
        "sentiment": "innovative logistics solution"
    }::jsonb,
    86.4,
    'Moderate Risk',
    'Technological Innovation and Liability',
    'Autonomous Vehicle Insurance',
    'ROBOT-2024-0007',
    4500.50,
    'Robot fleet coverage, liability protection, technological failure insurance'
),
(
    'Offshore wind turbine farm',
    '{
        "image_caption": "Multiple wind turbines installed in marine environment",
        "object_detection": {
            "turbine_count": 12,
            "marine_conditions": "challenging",
            "installation_complexity": "high"
        },
        "sentiment": "renewable energy infrastructure"
    }::jsonb,
    89.2,
    'High Risk',
    'Renewable Energy Marine Infrastructure',
    'Offshore Energy Insurance',
    'WIND-2024-0008',
    9800.75,
    'Marine environment protection, equipment replacement, operational disruption coverage'
),
(
    'Advanced agricultural precision farming equipment',
    '{
        "image_caption": "Sophisticated GPS-guided tractors and automated farming machinery",
        "object_detection": {
            "equipment_sophistication": "high-tech",
            "farming_area": "large scale",
            "technological_integration": "advanced"
        },
        "sentiment": "modern agricultural technology"
    }::jsonb,
    87.8,
    'Moderate Risk',
    'Agricultural Technology and Equipment',
    'Precision Farming Insurance',
    'FARM-2024-0009',
    3250.00,
    'Equipment replacement, technological failure coverage, crop protection'
),
(
    'Urban vertical farming facility',
    '{
        "image_caption": "Multi-level indoor vertical farming setup with hydroponic systems",
        "object_detection": {
            "farming_complexity": "advanced",
            "technology_level": "cutting-edge",
            "space_utilization": "optimal"
        },
        "sentiment": "innovative urban agriculture"
    }::jsonb,
    91.5,
    'Low Risk',
    'Urban Agricultural Infrastructure',
    'Innovative Farming Insurance',
    'VERTICAL-2024-0010',
    4750.25,
    'Facility protection, crop loss coverage, technological innovation insurance'
);

-- Create index for performance optimization
CREATE INDEX idx_insurance_transactions_risk ON insurance_transactions(risk_category);
CREATE INDEX idx_insurance_transactions_type ON insurance_transactions(insurance_type);
