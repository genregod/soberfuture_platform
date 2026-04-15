import { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, ScrollView, StyleSheet } from "react-native";
import { SafeAreaView } from "react-native-safe-area-context";

const MOODS = ["😔", "😕", "😐", "🙂", "😊"];

export default function CheckInScreen() {
  const [mood, setMood] = useState<number | null>(null);
  const [text, setText] = useState("");

  return (
    <SafeAreaView style={styles.safe}>
      <View style={styles.header}>
        <Text style={styles.title}>Today&apos;s check-in</Text>
      </View>

      <ScrollView contentContainerStyle={styles.body} keyboardShouldPersistTaps="handled">
        {/* Mood */}
        <Text style={styles.label}>How are you feeling right now?</Text>
        <View style={styles.moodRow}>
          {MOODS.map((emoji, i) => (
            <TouchableOpacity
              key={i}
              style={[styles.moodBtn, mood === i && styles.moodBtnActive]}
              onPress={() => setMood(i)}
            >
              <Text style={styles.moodEmoji}>{emoji}</Text>
            </TouchableOpacity>
          ))}
        </View>

        {/* Prompt */}
        <Text style={styles.label}>What&apos;s one thing you&apos;re grateful for today?</Text>
        <TextInput
          style={styles.textarea}
          multiline
          numberOfLines={5}
          placeholder="Write freely — this is just for you..."
          placeholderTextColor="#a1a1aa"
          value={text}
          onChangeText={setText}
          textAlignVertical="top"
        />

        <TouchableOpacity
          style={[styles.saveBtn, (!mood && !text) && styles.saveBtnDisabled]}
          disabled={!mood && !text}
        >
          <Text style={styles.saveBtnText}>Save entry</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safe: { flex: 1, backgroundColor: "#fff" },
  header: { paddingHorizontal: 20, paddingVertical: 14, borderBottomWidth: 1, borderBottomColor: "#f4f4f5" },
  title: { fontSize: 17, fontWeight: "600", color: "#18181b" },
  body: { padding: 20, gap: 16 },
  label: { fontSize: 14, fontWeight: "500", color: "#3f3f46" },
  moodRow: { flexDirection: "row", gap: 8 },
  moodBtn: { flex: 1, height: 56, borderRadius: 16, borderWidth: 1.5, borderColor: "#e4e4e7", alignItems: "center", justifyContent: "center" },
  moodBtnActive: { borderColor: "#4f46e5", backgroundColor: "#eef2ff" },
  moodEmoji: { fontSize: 24 },
  textarea: { borderWidth: 1.5, borderColor: "#e4e4e7", borderRadius: 16, padding: 14, fontSize: 14, color: "#18181b", minHeight: 120 },
  saveBtn: { backgroundColor: "#4f46e5", borderRadius: 16, height: 52, alignItems: "center", justifyContent: "center", marginTop: 8 },
  saveBtnDisabled: { opacity: 0.4 },
  saveBtnText: { color: "#fff", fontWeight: "600", fontSize: 16 },
});
