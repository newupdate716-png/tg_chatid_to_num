<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');

// কনফিগারেশন
$target_api = "https://devil-api.elementfx.com/api/tg-num.php?key=OWNBOT-JSCZUB&usersid=";
$group_link = "@publicgroup5s";
$dev_username = "@sakib01994";
$credit = "SB-SAKIB";

// ইনপুট চেক
$usersid = $_GET['usersid'] ?? '';

if (empty($usersid)) {
    // এপি প্যারামিটার না থাকলে প্রিমিয়াম এরর মেসেজ
    $error_response = [
        "status" => false,
        "message" => "API Request Failed! Invalid Parameters.",
        "instruction" => "Please provide a valid 'usersid' to fetch details.",
        "contact" => "Contact our Developer at $dev_username",
        "community" => $group_link
    ];
    echo json_encode($error_response, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
    exit;
}

// অরিজিনাল এপি থেকে ডেটা ফেচ করা
$final_url = $target_api . urlencode($usersid);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $final_url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);

if ($data && isset($data['status']) && $data['status'] === true) {
    // প্রিমিয়াম কাস্টম জেসন আউটপুট
    $output = [
        "status" => true,
        "results" => [
            "success" => true,
            "query" => $data['results']['query'] ?? $usersid,
            "result" => [
                "country" => $data['results']['result']['country'] ?? "Unknown",
                "country_code" => $data['results']['result']['country_code'] ?? "N/A",
                "number" => $data['results']['result']['number'] ?? "Not Found",
                "msg" => "Details successfully fetched by $credit"
            ]
        ],
        "branding" => [
            "api" => "SB-SAKIB",
            "developer" => $dev_username,
            "community" => $group_link,
            "credit" => $credit
        ],
        "system_status" => "Premium & Fast"
    ];
    echo json_encode($output, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
} else {
    // এপি ফেল হলে এরর মেসেজ
    $fail_response = [
        "status" => false,
        "message" => "Remote Server Error! API Failed.",
        "action" => "Contact $dev_username immediately for fix.",
        "group" => $group_link
    ];
    echo json_encode($fail_response, JSON_PRETTY_PRINT | JSON_UNESCAPED_SLASHES);
}
?>
