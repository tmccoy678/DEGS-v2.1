// Copyright 2026 The Sashiko Authors
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     https://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Modified: selected source excerpts assembled as an executable test oracle.
// Source pin/ranges: ../../provenance/sashiko-source.json
use serde::{Deserialize, Serialize};
use serde_json::{Value,json};
#[derive(Deserialize, Serialize, Debug, Clone, Default)]
pub struct StageConcernsOutput {
    #[serde(default)]
    pub concerns: Vec<Value>,
    #[serde(default)]
    pub dismissed_concerns: Vec<Value>,
}

#[derive(Deserialize, Serialize, Debug, Clone, Default)]
pub struct ConflictResolutionOutput {
    #[serde(default)]
    pub concerns: Vec<Value>,
}

#[derive(Deserialize, Serialize, Debug, Clone, Default)]
pub struct VerificationOutput {
    #[serde(default)]
    pub findings: Vec<Value>,
}
fn append_stage_items(
    dest: &mut Vec<Value>,
    src: &[Value],
    stage: &str,
    default_type: &str,
    _key: &str,
) {
    for item in src {
        let mut obj = item.clone();
        if let Some(map) = obj.as_object_mut() {
            if !map.contains_key("type")
                || map
                    .get("type")
                    .and_then(|v| v.as_str())
                    .unwrap_or("")
                    .is_empty()
            {
                map.insert("type".to_string(), json!(default_type));
            }
            map.insert("stage".to_string(), json!(stage));
        }
        dest.push(obj);
    }
}

fn append_stage_dismissed_concerns(dest: &mut Vec<Value>, src: &[Value], stage: &str) {
    for item in src {
        let mut obj = item.clone();
        if let Some(map) = obj.as_object_mut() {
            map.insert("stage".to_string(), json!(stage));
        }
        dest.push(obj);
    }
}

use std::io::{self, BufRead};
fn main() {
    for line in io::stdin().lock().lines() {
        let input: Value = serde_json::from_str(&line.unwrap()).unwrap();
        let result = match input["op"].as_str().unwrap() {
            "stage" => match serde_json::from_value::<StageConcernsOutput>(input["value"].clone()) { Ok(v) => json!({"ok":v}), Err(_) => json!({"error":true}) },
            "conflict" => match serde_json::from_value::<ConflictResolutionOutput>(input["value"].clone()) { Ok(v) => json!({"ok":v}), Err(_) => json!({"error":true}) },
            "verification" => match serde_json::from_value::<VerificationOutput>(input["value"].clone()) { Ok(v) => json!({"ok":v}), Err(_) => json!({"error":true}) },
            op => {
                let mut dest = input["dest"].as_array().unwrap().clone();
                let src = input["src"].as_array().unwrap();
                let stage = input["stage"].as_str().unwrap();
                if op == "dismissed" { append_stage_dismissed_concerns(&mut dest, src, stage); }
                else { append_stage_items(&mut dest, src, stage, "General", "description"); }
                json!({"ok":dest})
            }
        };
        println!("{}", result);
    }
}
